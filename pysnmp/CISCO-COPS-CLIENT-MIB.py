#
# PySNMP MIB module CISCO-COPS-CLIENT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-COPS-CLIENT-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:36:39 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, IpAddress, Integer32, iso, ObjectIdentity, MibIdentifier, Counter64, ModuleIdentity, TimeTicks, Counter32, NotificationType, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "IpAddress", "Integer32", "iso", "ObjectIdentity", "MibIdentifier", "Counter64", "ModuleIdentity", "TimeTicks", "Counter32", "NotificationType", "Bits")
DisplayString, TruthValue, RowStatus, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TruthValue", "RowStatus", "TextualConvention")
ciscoCopsClientMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 140))
ciscoCopsClientMIB.setRevisions(('2005-11-14 00:00', '2000-06-11 00:00', '1999-09-16 00:40',))
if mibBuilder.loadTexts: ciscoCopsClientMIB.setLastUpdated('200511140000Z')
if mibBuilder.loadTexts: ciscoCopsClientMIB.setOrganization('Cisco Systems Inc. ')
class CopsRole(TextualConvention, OctetString):
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(1, 31)

class CopsRoleCombination(TextualConvention, OctetString):
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 255)

class CopsDomainName(TextualConvention, OctetString):
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 31)

class CopsClientType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("rsvp", 1), ("provisioning", 2))

ccopsMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 140, 1))
ccopsGlobalObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 140, 1, 1))
ccopsServerMax = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 140, 1, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setUnits('servers').setMaxAccess("readonly")
if mibBuilder.loadTexts: ccopsServerMax.setStatus('current')
ccopsMaxRole = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 140, 1, 1, 2), Unsigned32()).setUnits('roles').setMaxAccess("readonly")
if mibBuilder.loadTexts: ccopsMaxRole.setStatus('current')
ccopsMaxRoleCombination = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 140, 1, 1, 3), Unsigned32()).setUnits('role-combinations').setMaxAccess("readonly")
if mibBuilder.loadTexts: ccopsMaxRoleCombination.setStatus('current')
ccopsServerConfigTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 140, 1, 1, 4), )
if mibBuilder.loadTexts: ccopsServerConfigTable.setStatus('current')
ccopsServerConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 140, 1, 1, 4, 1), ).setIndexNames((0, "CISCO-COPS-CLIENT-MIB", "ccopsServerConfigClientType"), (1, "CISCO-COPS-CLIENT-MIB", "ccopsServerConfigName"))
if mibBuilder.loadTexts: ccopsServerConfigEntry.setStatus('current')
ccopsServerConfigClientType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 140, 1, 1, 4, 1, 1), CopsClientType())
if mibBuilder.loadTexts: ccopsServerConfigClientType.setStatus('current')
ccopsServerConfigName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 140, 1, 1, 4, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 64)))
if mibBuilder.loadTexts: ccopsServerConfigName.setStatus('current')
ccopsServerConfigPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 140, 1, 1, 4, 1, 3), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ccopsServerConfigPriority.setStatus('current')
ccopsServerConfigPort = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 140, 1, 1, 4, 1, 4), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535)).clone(3288)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ccopsServerConfigPort.setStatus('current')
ccopsServerConfigStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 140, 1, 1, 4, 1, 5), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ccopsServerConfigStatus.setStatus('current')
ccopsInitialTimeout = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 140, 1, 1, 5), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535)).clone(30)).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: ccopsInitialTimeout.setStatus('current')
ccopsTimeoutIncrement = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 140, 1, 1, 6), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535)).clone(30)).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: ccopsTimeoutIncrement.setStatus('current')
ccopsTimeoutMax = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 140, 1, 1, 7), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535)).clone(300)).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: ccopsTimeoutMax.setStatus('current')
ccopsDomainTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 140, 1, 1, 8), )
if mibBuilder.loadTexts: ccopsDomainTable.setStatus('current')
ccopsDomainEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 140, 1, 1, 8, 1), ).setIndexNames((0, "CISCO-COPS-CLIENT-MIB", "ccopsDomainClientType"))
if mibBuilder.loadTexts: ccopsDomainEntry.setStatus('current')
ccopsDomainClientType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 140, 1, 1, 8, 1, 1), CopsClientType())
if mibBuilder.loadTexts: ccopsDomainClientType.setStatus('current')
ccopsDomainName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 140, 1, 1, 8, 1, 2), CopsDomainName().clone(hexValue="")).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ccopsDomainName.setStatus('current')
ccopsRoleTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 140, 1, 1, 9), )
if mibBuilder.loadTexts: ccopsRoleTable.setStatus('current')
ccopsRoleEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 140, 1, 1, 9, 1), ).setIndexNames((1, "CISCO-COPS-CLIENT-MIB", "ccopsRoleName"))
if mibBuilder.loadTexts: ccopsRoleEntry.setStatus('current')
ccopsRoleName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 140, 1, 1, 9, 1, 1), CopsRole())
if mibBuilder.loadTexts: ccopsRoleName.setStatus('current')
ccopsRoleStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 140, 1, 1, 9, 1, 2), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ccopsRoleStatus.setStatus('current')
ccopsIfTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 140, 1, 1, 10), )
if mibBuilder.loadTexts: ccopsIfTable.setStatus('current')
ccopsIfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 140, 1, 1, 10, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: ccopsIfEntry.setStatus('current')
ccopsIfRoleCombination = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 140, 1, 1, 10, 1, 1), CopsRoleCombination()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ccopsIfRoleCombination.setStatus('current')
ccopsRoleConfigSupported = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 140, 1, 1, 11), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ccopsRoleConfigSupported.setStatus('current')
ccopsMIBNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 140, 2))
ccopsMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 140, 3))
ccopsMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 140, 3, 1))
ccopsMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 140, 3, 2))
ccopsMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 140, 3, 1, 1)).setObjects(("CISCO-COPS-CLIENT-MIB", "ccopsGlobalGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ccopsMIBCompliance = ccopsMIBCompliance.setStatus('deprecated')
ccopsMIBComplianceRev2 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 140, 3, 1, 2)).setObjects(("CISCO-COPS-CLIENT-MIB", "ccopsGlobalGroupRev2"), ("CISCO-COPS-CLIENT-MIB", "ccopsRoleGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ccopsMIBComplianceRev2 = ccopsMIBComplianceRev2.setStatus('current')
ccopsGlobalGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 140, 3, 2, 1)).setObjects(("CISCO-COPS-CLIENT-MIB", "ccopsServerMax"), ("CISCO-COPS-CLIENT-MIB", "ccopsServerConfigPriority"), ("CISCO-COPS-CLIENT-MIB", "ccopsServerConfigPort"), ("CISCO-COPS-CLIENT-MIB", "ccopsServerConfigStatus"), ("CISCO-COPS-CLIENT-MIB", "ccopsInitialTimeout"), ("CISCO-COPS-CLIENT-MIB", "ccopsTimeoutIncrement"), ("CISCO-COPS-CLIENT-MIB", "ccopsTimeoutMax"), ("CISCO-COPS-CLIENT-MIB", "ccopsDomainName"), ("CISCO-COPS-CLIENT-MIB", "ccopsMaxRole"), ("CISCO-COPS-CLIENT-MIB", "ccopsMaxRoleCombination"), ("CISCO-COPS-CLIENT-MIB", "ccopsRoleStatus"), ("CISCO-COPS-CLIENT-MIB", "ccopsIfRoleCombination"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ccopsGlobalGroup = ccopsGlobalGroup.setStatus('deprecated')
ccopsGlobalGroupRev2 = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 140, 3, 2, 2)).setObjects(("CISCO-COPS-CLIENT-MIB", "ccopsServerMax"), ("CISCO-COPS-CLIENT-MIB", "ccopsServerConfigPriority"), ("CISCO-COPS-CLIENT-MIB", "ccopsServerConfigPort"), ("CISCO-COPS-CLIENT-MIB", "ccopsServerConfigStatus"), ("CISCO-COPS-CLIENT-MIB", "ccopsInitialTimeout"), ("CISCO-COPS-CLIENT-MIB", "ccopsTimeoutIncrement"), ("CISCO-COPS-CLIENT-MIB", "ccopsTimeoutMax"), ("CISCO-COPS-CLIENT-MIB", "ccopsDomainName"), ("CISCO-COPS-CLIENT-MIB", "ccopsMaxRoleCombination"), ("CISCO-COPS-CLIENT-MIB", "ccopsIfRoleCombination"), ("CISCO-COPS-CLIENT-MIB", "ccopsRoleConfigSupported"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ccopsGlobalGroupRev2 = ccopsGlobalGroupRev2.setStatus('current')
ccopsRoleGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 140, 3, 2, 3)).setObjects(("CISCO-COPS-CLIENT-MIB", "ccopsMaxRole"), ("CISCO-COPS-CLIENT-MIB", "ccopsRoleStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ccopsRoleGroup = ccopsRoleGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-COPS-CLIENT-MIB", ccopsServerConfigTable=ccopsServerConfigTable, PYSNMP_MODULE_ID=ciscoCopsClientMIB, ccopsDomainName=ccopsDomainName, ccopsRoleTable=ccopsRoleTable, ccopsRoleName=ccopsRoleName, ccopsIfEntry=ccopsIfEntry, ccopsServerConfigPriority=ccopsServerConfigPriority, ccopsServerConfigName=ccopsServerConfigName, CopsClientType=CopsClientType, ccopsRoleConfigSupported=ccopsRoleConfigSupported, ccopsRoleStatus=ccopsRoleStatus, ccopsIfRoleCombination=ccopsIfRoleCombination, ccopsServerMax=ccopsServerMax, ccopsGlobalGroupRev2=ccopsGlobalGroupRev2, ccopsRoleGroup=ccopsRoleGroup, ccopsGlobalGroup=ccopsGlobalGroup, ccopsTimeoutMax=ccopsTimeoutMax, ccopsMIBConformance=ccopsMIBConformance, ccopsIfTable=ccopsIfTable, ccopsMaxRoleCombination=ccopsMaxRoleCombination, ccopsMIBNotifications=ccopsMIBNotifications, ccopsInitialTimeout=ccopsInitialTimeout, ccopsRoleEntry=ccopsRoleEntry, ciscoCopsClientMIB=ciscoCopsClientMIB, CopsRole=CopsRole, CopsRoleCombination=CopsRoleCombination, ccopsDomainEntry=ccopsDomainEntry, ccopsServerConfigEntry=ccopsServerConfigEntry, ccopsMIBGroups=ccopsMIBGroups, ccopsMIBComplianceRev2=ccopsMIBComplianceRev2, ccopsServerConfigStatus=ccopsServerConfigStatus, ccopsServerConfigClientType=ccopsServerConfigClientType, ccopsDomainTable=ccopsDomainTable, ccopsServerConfigPort=ccopsServerConfigPort, ccopsMaxRole=ccopsMaxRole, ccopsMIBCompliances=ccopsMIBCompliances, ccopsGlobalObjects=ccopsGlobalObjects, ccopsDomainClientType=ccopsDomainClientType, ccopsMIBObjects=ccopsMIBObjects, ccopsTimeoutIncrement=ccopsTimeoutIncrement, CopsDomainName=CopsDomainName, ccopsMIBCompliance=ccopsMIBCompliance)
