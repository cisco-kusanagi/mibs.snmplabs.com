#
# PySNMP MIB module CISCOSB-SCT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCOSB-SCT-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:07:20 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion")
switch001, = mibBuilder.importSymbols("CISCOSB-MIB", "switch001")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Integer32, IpAddress, MibIdentifier, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, TimeTicks, ModuleIdentity, NotificationType, Counter32, ObjectIdentity, Unsigned32, Counter64, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "IpAddress", "MibIdentifier", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "TimeTicks", "ModuleIdentity", "NotificationType", "Counter32", "ObjectIdentity", "Unsigned32", "Counter64", "iso")
DisplayString, TruthValue, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TruthValue", "TextualConvention")
rlSctMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 203))
if mibBuilder.loadTexts: rlSctMib.setLastUpdated('201008161234Z')
if mibBuilder.loadTexts: rlSctMib.setOrganization('Cisco Small Business')
rlSctCpuRateEnabled = MibScalar((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 203, 1), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlSctCpuRateEnabled.setStatus('current')
rlSctCpuRate = MibScalar((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 203, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlSctCpuRate.setStatus('current')
mibBuilder.exportSymbols("CISCOSB-SCT-MIB", rlSctCpuRate=rlSctCpuRate, rlSctMib=rlSctMib, PYSNMP_MODULE_ID=rlSctMib, rlSctCpuRateEnabled=rlSctCpuRateEnabled)
