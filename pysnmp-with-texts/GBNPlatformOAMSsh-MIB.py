#
# PySNMP MIB module GBNPlatformOAMSsh-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/GBNPlatformOAMSsh-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:18:35 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint")
gbnPlatformOAM, = mibBuilder.importSymbols("GBNPlatformOAM-MIB", "gbnPlatformOAM")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
snmpTraps, = mibBuilder.importSymbols("SNMPv2-MIB", "snmpTraps")
TimeTicks, Bits, IpAddress, NotificationType, MibIdentifier, ModuleIdentity, Integer32, Counter32, Counter64, ObjectIdentity, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "Bits", "IpAddress", "NotificationType", "MibIdentifier", "ModuleIdentity", "Integer32", "Counter32", "Counter64", "ObjectIdentity", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "iso")
DisplayString, TextualConvention, TruthValue, MacAddress, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "TruthValue", "MacAddress", "RowStatus")
gbnPlatformOAMSsh = ModuleIdentity((1, 3, 6, 1, 4, 1, 13464, 1, 2, 1, 1, 11))
gbnPlatformOAMSsh.setRevisions(('1905-05-25 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: gbnPlatformOAMSsh.setRevisionsDescriptions(('Initial MIB creation.',))
if mibBuilder.loadTexts: gbnPlatformOAMSsh.setLastUpdated('0505250000Z')
if mibBuilder.loadTexts: gbnPlatformOAMSsh.setOrganization('Greentech')
if mibBuilder.loadTexts: gbnPlatformOAMSsh.setContactInfo('Adam Armstrong E-mail: adama@observium.org')
if mibBuilder.loadTexts: gbnPlatformOAMSsh.setDescription('Ssh mib definition.')
sshVersion = MibScalar((1, 3, 6, 1, 4, 1, 13464, 1, 2, 1, 1, 11, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("v1", 1), ("v2", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sshVersion.setStatus('current')
if mibBuilder.loadTexts: sshVersion.setDescription('SSH version.')
sshState = MibScalar((1, 3, 6, 1, 4, 1, 13464, 1, 2, 1, 1, 11, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sshState.setStatus('current')
if mibBuilder.loadTexts: sshState.setDescription('enable or disable SSH.')
sshKeyAvailable = MibScalar((1, 3, 6, 1, 4, 1, 13464, 1, 2, 1, 1, 11, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("available", 1), ("unavailable", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sshKeyAvailable.setStatus('current')
if mibBuilder.loadTexts: sshKeyAvailable.setDescription('SSH key file state.')
mibBuilder.exportSymbols("GBNPlatformOAMSsh-MIB", gbnPlatformOAMSsh=gbnPlatformOAMSsh, sshVersion=sshVersion, sshState=sshState, PYSNMP_MODULE_ID=gbnPlatformOAMSsh, sshKeyAvailable=sshKeyAvailable)
