#
# PySNMP MIB module NETWORK-ALCHEMY-CONFIG-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/NETWORK-ALCHEMY-CONFIG-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:11:09 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint")
config, netalModules = mibBuilder.importSymbols("NETAL-SMI", "config", "netalModules")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
iso, TimeTicks, ModuleIdentity, Bits, Unsigned32, Counter32, Gauge32, NotificationType, Integer32, IpAddress, MibIdentifier, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "TimeTicks", "ModuleIdentity", "Bits", "Unsigned32", "Counter32", "Gauge32", "NotificationType", "Integer32", "IpAddress", "MibIdentifier", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
networkAlchemyConfigMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 2972, 5, 6))
networkAlchemyConfigMIB.setRevisions(('1900-08-30 00:00',))
if mibBuilder.loadTexts: networkAlchemyConfigMIB.setLastUpdated('0003140000Z')
if mibBuilder.loadTexts: networkAlchemyConfigMIB.setOrganization('Network Alchemy, Inc.')
configDirtyBit = MibScalar((1, 3, 6, 1, 4, 1, 2972, 2, 5, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("no", 0), ("yes", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: configDirtyBit.setStatus('current')
configCommit = MibScalar((1, 3, 6, 1, 4, 1, 2972, 2, 5, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("no", 0), ("yes", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: configCommit.setStatus('current')
mibBuilder.exportSymbols("NETWORK-ALCHEMY-CONFIG-MIB", configDirtyBit=configDirtyBit, PYSNMP_MODULE_ID=networkAlchemyConfigMIB, networkAlchemyConfigMIB=networkAlchemyConfigMIB, configCommit=configCommit)
