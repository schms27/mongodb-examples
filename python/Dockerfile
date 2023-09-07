# Container for building the environment
FROM condaforge/mambaforge:4.9.2-5 as conda

COPY environment-linux-64.lock .
RUN mamba create --copy -p /env --file environment-linux-64.lock && conda clean -afy
RUN ls
COPY . /pkg
RUN conda run -p /env python -m pip install --no-deps /pkg

# Distroless for execution
FROM gcr.io/distroless/base-debian10

COPY --from=conda /env /env

CMD [ \
  "/env/bin/gunicorn", "-b", "0.0.0.0:8000", "-k", "uvicorn.workers.UvicornWorker", "api.main:app" \
]