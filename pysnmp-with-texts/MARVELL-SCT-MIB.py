#
# PySNMP MIB module MARVELL-SCT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/MARVELL-SCT-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:10:15 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion")
rnd, = mibBuilder.importSymbols("RADLAN-MIB", "rnd")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
MibIdentifier, iso, Integer32, Bits, Counter64, NotificationType, ObjectIdentity, Counter32, Gauge32, ModuleIdentity, Unsigned32, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "iso", "Integer32", "Bits", "Counter64", "NotificationType", "ObjectIdentity", "Counter32", "Gauge32", "ModuleIdentity", "Unsigned32", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress")
TextualConvention, TruthValue, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "TruthValue", "DisplayString")
rlSctMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 89, 203))
if mibBuilder.loadTexts: rlSctMib.setLastUpdated('201008161234Z')
if mibBuilder.loadTexts: rlSctMib.setOrganization('MARVELL Semiconductor, Inc.')
if mibBuilder.loadTexts: rlSctMib.setContactInfo('www.marvell.com')
if mibBuilder.loadTexts: rlSctMib.setDescription('The private MIB module definition for SCT MIB.')
rlSctCpuRateEnabled = MibScalar((1, 3, 6, 1, 4, 1, 89, 203, 1), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlSctCpuRateEnabled.setStatus('current')
if mibBuilder.loadTexts: rlSctCpuRateEnabled.setDescription('Indication whether the counter CPU rate is enabled')
rlSctCpuRate = MibScalar((1, 3, 6, 1, 4, 1, 89, 203, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlSctCpuRate.setStatus('current')
if mibBuilder.loadTexts: rlSctCpuRate.setDescription('the amount of packets per second the CPU is handling.')
mibBuilder.exportSymbols("MARVELL-SCT-MIB", rlSctMib=rlSctMib, rlSctCpuRate=rlSctCpuRate, rlSctCpuRateEnabled=rlSctCpuRateEnabled, PYSNMP_MODULE_ID=rlSctMib)
