#
# PySNMP MIB module Dell-rlNicRedundancy (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Dell-rlNicRedundancy
# Produced by pysmi-0.3.4 at Mon Apr 29 18:43:07 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
rnd, = mibBuilder.importSymbols("Dell-MIB", "rnd")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Bits, Integer32, ModuleIdentity, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, IpAddress, TimeTicks, Counter64, NotificationType, ObjectIdentity, Gauge32, Unsigned32, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Integer32", "ModuleIdentity", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "IpAddress", "TimeTicks", "Counter64", "NotificationType", "ObjectIdentity", "Gauge32", "Unsigned32", "MibIdentifier")
TruthValue, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "TextualConvention", "DisplayString")
rlNicRedundancy = ModuleIdentity((1, 3, 6, 1, 4, 1, 89, 105))
rlNicRedundancy.setRevisions(('2005-06-16 00:00',))
if mibBuilder.loadTexts: rlNicRedundancy.setLastUpdated('200506160000Z')
if mibBuilder.loadTexts: rlNicRedundancy.setOrganization('Dell')
rlNicRedundancyEnable = MibScalar((1, 3, 6, 1, 4, 1, 89, 105, 1), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlNicRedundancyEnable.setStatus('current')
mibBuilder.exportSymbols("Dell-rlNicRedundancy", PYSNMP_MODULE_ID=rlNicRedundancy, rlNicRedundancyEnable=rlNicRedundancyEnable, rlNicRedundancy=rlNicRedundancy)
