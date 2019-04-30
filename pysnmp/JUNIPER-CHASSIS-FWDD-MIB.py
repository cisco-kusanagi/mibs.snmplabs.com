#
# PySNMP MIB module JUNIPER-CHASSIS-FWDD-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/JUNIPER-CHASSIS-FWDD-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:47:58 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion")
jnxMibs, = mibBuilder.importSymbols("JUNIPER-SMI", "jnxMibs")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, Gauge32, Counter32, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, iso, ObjectIdentity, Counter64, NotificationType, ModuleIdentity, Bits, TimeTicks, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "Gauge32", "Counter32", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "iso", "ObjectIdentity", "Counter64", "NotificationType", "ModuleIdentity", "Bits", "TimeTicks", "Integer32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
jnxFwdd = ModuleIdentity((1, 3, 6, 1, 4, 1, 2636, 3, 34))
if mibBuilder.loadTexts: jnxFwdd.setLastUpdated('200602162158Z')
if mibBuilder.loadTexts: jnxFwdd.setOrganization('Juniper Networks, Inc.')
jnxFwddProcess = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 3, 34, 1))
jnxFwddMicroKernelCPUUsage = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 34, 1, 1), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxFwddMicroKernelCPUUsage.setStatus('current')
jnxFwddRtThreadsCPUUsage = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 34, 1, 2), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxFwddRtThreadsCPUUsage.setStatus('current')
jnxFwddHeapUsage = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 34, 1, 3), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxFwddHeapUsage.setStatus('current')
jnxFwddDmaMemUsage = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 34, 1, 4), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxFwddDmaMemUsage.setStatus('current')
jnxFwddUpTime = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 34, 1, 5), Integer32()).setUnits('seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxFwddUpTime.setStatus('current')
mibBuilder.exportSymbols("JUNIPER-CHASSIS-FWDD-MIB", jnxFwddUpTime=jnxFwddUpTime, jnxFwddMicroKernelCPUUsage=jnxFwddMicroKernelCPUUsage, PYSNMP_MODULE_ID=jnxFwdd, jnxFwddHeapUsage=jnxFwddHeapUsage, jnxFwddRtThreadsCPUUsage=jnxFwddRtThreadsCPUUsage, jnxFwdd=jnxFwdd, jnxFwddProcess=jnxFwddProcess, jnxFwddDmaMemUsage=jnxFwddDmaMemUsage)
