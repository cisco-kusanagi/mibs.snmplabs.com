#
# PySNMP MIB module GBNPlatformOAMSsh-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/GBNPlatformOAMSsh-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:05:04 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint")
gbnPlatformOAM, = mibBuilder.importSymbols("GBNPlatformOAM-MIB", "gbnPlatformOAM")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
snmpTraps, = mibBuilder.importSymbols("SNMPv2-MIB", "snmpTraps")
IpAddress, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, Counter64, Gauge32, iso, MibIdentifier, NotificationType, TimeTicks, ModuleIdentity, Integer32, Unsigned32, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "Counter64", "Gauge32", "iso", "MibIdentifier", "NotificationType", "TimeTicks", "ModuleIdentity", "Integer32", "Unsigned32", "Counter32")
TruthValue, TextualConvention, DisplayString, RowStatus, MacAddress = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "TextualConvention", "DisplayString", "RowStatus", "MacAddress")
gbnPlatformOAMSsh = ModuleIdentity((1, 3, 6, 1, 4, 1, 13464, 1, 2, 1, 1, 11))
gbnPlatformOAMSsh.setRevisions(('1905-05-25 00:00',))
if mibBuilder.loadTexts: gbnPlatformOAMSsh.setLastUpdated('0505250000Z')
if mibBuilder.loadTexts: gbnPlatformOAMSsh.setOrganization('Greentech')
sshVersion = MibScalar((1, 3, 6, 1, 4, 1, 13464, 1, 2, 1, 1, 11, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("v1", 1), ("v2", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sshVersion.setStatus('current')
sshState = MibScalar((1, 3, 6, 1, 4, 1, 13464, 1, 2, 1, 1, 11, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sshState.setStatus('current')
sshKeyAvailable = MibScalar((1, 3, 6, 1, 4, 1, 13464, 1, 2, 1, 1, 11, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("available", 1), ("unavailable", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sshKeyAvailable.setStatus('current')
mibBuilder.exportSymbols("GBNPlatformOAMSsh-MIB", sshState=sshState, gbnPlatformOAMSsh=gbnPlatformOAMSsh, PYSNMP_MODULE_ID=gbnPlatformOAMSsh, sshKeyAvailable=sshKeyAvailable, sshVersion=sshVersion)
