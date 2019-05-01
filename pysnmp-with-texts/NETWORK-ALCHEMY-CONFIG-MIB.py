#
# PySNMP MIB module NETWORK-ALCHEMY-CONFIG-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/NETWORK-ALCHEMY-CONFIG-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:20:54 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
config, netalModules = mibBuilder.importSymbols("NETAL-SMI", "config", "netalModules")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Unsigned32, ModuleIdentity, Bits, TimeTicks, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, iso, Gauge32, Integer32, Counter32, ObjectIdentity, IpAddress, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "ModuleIdentity", "Bits", "TimeTicks", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "iso", "Gauge32", "Integer32", "Counter32", "ObjectIdentity", "IpAddress", "NotificationType")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
networkAlchemyConfigMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 2972, 5, 6))
networkAlchemyConfigMIB.setRevisions(('1900-08-30 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: networkAlchemyConfigMIB.setRevisionsDescriptions(('Placeholder for the HP Open View NNM SNMP browser.',))
if mibBuilder.loadTexts: networkAlchemyConfigMIB.setLastUpdated('0003140000Z')
if mibBuilder.loadTexts: networkAlchemyConfigMIB.setOrganization('Network Alchemy, Inc.')
if mibBuilder.loadTexts: networkAlchemyConfigMIB.setContactInfo(' Network Alchemy Customer Support Postal: 1538 Pacific Av. Santa Cruz, CA 95060 USA E-Mail: snmp-contact@network-alchemy.com')
if mibBuilder.loadTexts: networkAlchemyConfigMIB.setDescription('Crypto Cluster Configuration MIB module.')
configDirtyBit = MibScalar((1, 3, 6, 1, 4, 1, 2972, 2, 5, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("no", 0), ("yes", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: configDirtyBit.setStatus('current')
if mibBuilder.loadTexts: configDirtyBit.setDescription('Says whether the configuration has been changed via a set on any of the writable SNMP variables.')
configCommit = MibScalar((1, 3, 6, 1, 4, 1, 2972, 2, 5, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("no", 0), ("yes", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: configCommit.setStatus('current')
if mibBuilder.loadTexts: configCommit.setDescription('When an SNMP management station sets (changes) a configuration parameter via an SNMP set operation, the SNMP agent code will set a dirt bit. The management station can then submit a set operation on this configCommit variable to write the configuration to flash, thereby committing the change. Performing a read on this variable will return the value of the config dirty bit.')
mibBuilder.exportSymbols("NETWORK-ALCHEMY-CONFIG-MIB", PYSNMP_MODULE_ID=networkAlchemyConfigMIB, configDirtyBit=configDirtyBit, configCommit=configCommit, networkAlchemyConfigMIB=networkAlchemyConfigMIB)
