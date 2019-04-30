#
# PySNMP MIB module MARVELL-SCT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/MARVELL-SCT-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:59:52 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint")
rnd, = mibBuilder.importSymbols("RADLAN-MIB", "rnd")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Counter64, Counter32, Unsigned32, NotificationType, ObjectIdentity, ModuleIdentity, IpAddress, MibIdentifier, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Gauge32, Integer32, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "Counter32", "Unsigned32", "NotificationType", "ObjectIdentity", "ModuleIdentity", "IpAddress", "MibIdentifier", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Gauge32", "Integer32", "Bits")
TruthValue, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "TextualConvention", "DisplayString")
rlSctMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 89, 203))
if mibBuilder.loadTexts: rlSctMib.setLastUpdated('201008161234Z')
if mibBuilder.loadTexts: rlSctMib.setOrganization('MARVELL Semiconductor, Inc.')
rlSctCpuRateEnabled = MibScalar((1, 3, 6, 1, 4, 1, 89, 203, 1), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlSctCpuRateEnabled.setStatus('current')
rlSctCpuRate = MibScalar((1, 3, 6, 1, 4, 1, 89, 203, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlSctCpuRate.setStatus('current')
mibBuilder.exportSymbols("MARVELL-SCT-MIB", rlSctCpuRate=rlSctCpuRate, rlSctCpuRateEnabled=rlSctCpuRateEnabled, PYSNMP_MODULE_ID=rlSctMib, rlSctMib=rlSctMib)
