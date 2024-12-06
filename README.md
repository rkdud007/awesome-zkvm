<div align="center">
  <h1 align="center">awesome zkVm</h1>

A curated list of zkVM, zero-knowledge virtual machine.

  <p align="center">
    <a href="https://github.com/sindresorhus/awesome">
      <img alt="awesome list badge" src="https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg">
    </a>
    <a href="https://github.com/rkdud007/awesome-zkvm/graphs/contributors">
      <img alt="GitHub contributors" src="https://img.shields.io/github/contributors/rkdud007/awesome-zkvm">
    </a>
    <a href="http://makeapullrequest.com">
      <img alt="pull requests welcome badge" src="https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat">
    </a>
  </p>

</div>

[Contributions](./CONTRIBUTING.md) and suggestions are always welcome; open issues or pull requests with any changes you want to be made.

# contents

- [projects repositories](#projects-repositories)
- [bench](#bench)
- [papers](#papers)
- [resources](#resources)
- [tutorials](#tutorials)
- [architecture](#architecture)
  - [precompiles](#precompiles)
  - [recursion](#recursion)
  - [lookup arguments](#lookup-arguments)
  - [hardware](#hardware)
- [related awesome lists](#related-awesome-lists)

## projects 

| zkVM                                                             | Release | ISA    | Continuations      | GPU | Parallel Proving |
|:----------------------------------------------------------------:|:-------:|:------:|:------------------:|:---:|:----------------:|
| [cairo](https://github.com/lambdaclass/cairo-vm)                 | v1.0.1 | Cairo  |                    |     |                  |
| [ceno](https://github.com/scroll-tech/ceno)                      |  | RISC-V |                    |     |                  |
| [eigen zkvm](https://github.com/0xEigenLabs/eigen-zkvm)          | v0.0.5 | RISC-V |                    |     |                  |
| [jolt](https://github.com/a16z/jolt)                             |  | RISC-V | :x:                |     |                  |
| [miden](https://github.com/0xPolygonMiden/miden-vm)              | v0.11.0 | Wasm   |                    |     |                  |
| [mozak vm](https://github.com/0xmozak/mozak-vm)                  | v0.1 | RISC-V |                    |     |                  |
| [nexus](https://github.com/nexus-xyz/nexus-zkvm)                 |  | RISC-V | :heavy_check_mark: |     |                  |
| [o1vm](https://github.com/o1-labs/proof-systems/tree/master/o1vm)|  | MIPS   |                    |     |                  |
| [olavm](https://github.com/Sin7Y/olavm)                          | testnet-alpha | Custom |                    |     |                  |
| [powdr](https://github.com/powdr-labs/powdr)                     | v0.1.2 | RISC-V | :heavy_check_mark: |     |                  |
| [risc0](https://github.com/risc0/risc0)                          | v1.2.0 | RISC-V | :heavy_check_mark: |     |                  |
| [sp1](https://github.com/succinctlabs/sp1)                       | v4.0.0-rc.1 | RISC-V | :heavy_check_mark: |     |                  |
| [sphinx](https://github.com/argumentcomputer/sphinx)             | v1.0.0 |        |                    |     |                  |
| [triton vm](https://github.com/TritonVM/triton-vm)               | v0.43.0 | Custom |                    |     |                  |
| [valida](https://github.com/valida-xyz/valida)                   |  | Valida | :x:                |     |                  |
| [zisk](https://github.com/0xPolygonHermez/zisk)                  | nightly-5df9a3679cd2a728fcad21730e0c1d12b642ff21 | RISC-V |                    |     |                  |
| [zkWasm](https://github.com/DelphinusLab/zkWasm)                 |  | Wasm   | :heavy_check_mark: |     |                  |
| [zkm](https://github.com/zkMIPS/zkm)                             |  | MIPS   | :heavy_check_mark: |     |                  |
- [benchmarks (lita)](https://lita.gitbook.io/lita-documentation/architecture/benchmarks) | [code](https://github.com/lita-xyz/benchmarks)
- [benchmark (risc0)](https://reports.risczero.com/benchmarks/Linux-cpu) | [code](https://github.com/risc0/risc0/tree/main/benchmarks) 
- zkvm-benchmarks (a16z) | [code](https://github.com/a16z/zkvm-benchmarks)
- zkvm perf (succinct) | [code](https://github.com/succinctlabs/zkvm-perf)
- [~tacryt-socryp on Zorp, the Nock zkVM | Reassembly23](https://www.youtube.com/watch?v=zD45V6GAD00)

*Release versions last updated: 2024-12-06 19:52 UTC*

## tutorials

- [brainfuck tutorial](https://neptune.cash/learn/brainfuck-tutorial/)
- [continuous read  only memory constraints an implementation using lambdaworks](https://blog.lambdaclass.com/continuous-read-only-memory-constraints-an-implementation-using-lambdaworks/)
- [fri from scratch](https://blog.lambdaclass.com/how-to-code-fri-from-scratch/)
- [stark by hand](https://dev.risczero.com/proof-system/stark-by-hand)
- [stark brainfuck](https://aszepieniec.github.io/stark-brainfuck/)
- [stark 101](https://starkware.co/stark-101/)

## related awesome lists

- [awesome risc0](https://github.com/inversebrah/awesome-risc0)
- [awesome sp1](https://github.com/gakonst/awesome-sp1)
- [awesome starknet #cryptography-and-maths](https://github.com/keep-starknet-strange/awesome-starknet?tab=readme-ov-file#cryptography-and-maths)
- [awesome zkp](https://github.com/matter-labs/awesome-zero-knowledge-proofs)
