#
# PySNMP MIB module HPVCMODULE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HPVCMODULE-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:30:30 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion")
ifIndex, ifOutErrors, ifInErrors = mibBuilder.importSymbols("IF-MIB", "ifIndex", "ifOutErrors", "ifInErrors")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
IpAddress, iso, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, enterprises, Gauge32, Counter64, MibIdentifier, TimeTicks, ObjectIdentity, ModuleIdentity, NotificationType, Integer32, Counter32, Unsigned32, zeroDotZero, mib_2 = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "iso", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "enterprises", "Gauge32", "Counter64", "MibIdentifier", "TimeTicks", "ObjectIdentity", "ModuleIdentity", "NotificationType", "Integer32", "Counter32", "Unsigned32", "zeroDotZero", "mib-2")
DisplayString, TextualConvention, RowPointer, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "RowPointer", "TruthValue")
TransportAddress, TransportAddressType = mibBuilder.importSymbols("TRANSPORT-ADDRESS-MIB", "TransportAddress", "TransportAddressType")
hp = MibIdentifier((1, 3, 6, 1, 4, 1, 11))
hpSysMgt = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 5))
hpEmbeddedServerMgt = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 5, 7))
hpModuleMgmtProc = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 5, 7, 5))
virtualConnect = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 2))
vcModuleMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 2, 3))
vcModuleMIB.setRevisions(('2008-10-08 00:00', '2009-02-18 00:00',))
if mibBuilder.loadTexts: vcModuleMIB.setLastUpdated('200809160000Z')
if mibBuilder.loadTexts: vcModuleMIB.setOrganization('Hewlett-Packard Company')
vcModuleMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 2, 3, 1))
vcModuleObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 2, 3, 1, 1))
class VcModuleRole(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("unintegrated", 1), ("primaryProtected", 2), ("primaryUnprotected", 3), ("standby", 4), ("other", 5))

class VcEnclosureRole(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("unknown", 1), ("primary", 2), ("secondary", 3))

class VcModuleType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("vcModuleEnet", 1), ("vcModuleFC", 2), ("vcModuleOther", 3))

vcModuleDomainName = MibScalar((1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 2, 3, 1, 1, 1), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vcModuleDomainName.setStatus('current')
vcModuleRole = MibScalar((1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 2, 3, 1, 1, 2), VcModuleRole()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vcModuleRole.setStatus('current')
vcModuleDomainPrimaryAddressType = MibScalar((1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 2, 3, 1, 1, 3), TransportAddressType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vcModuleDomainPrimaryAddressType.setStatus('current')
vcModuleDomainPrimaryAddress = MibScalar((1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 2, 3, 1, 1, 4), TransportAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vcModuleDomainPrimaryAddress.setStatus('current')
vcModuleEnclosureRole = MibScalar((1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 2, 3, 1, 1, 5), VcEnclosureRole()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vcModuleEnclosureRole.setStatus('current')
vcModuleMIBNotificationPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 2, 3, 2))
vcModuleMIBNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 2, 3, 2, 0))
vcModuleMIBNotificationObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 2, 3, 2, 1))
vcModuleDomainRoleChange = NotificationType((1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 2, 3, 2, 0, 1)).setObjects(("HPVCMODULE-MIB", "vcModuleRole"))
if mibBuilder.loadTexts: vcModuleDomainRoleChange.setStatus('current')
vcModPortInputUtilizationUp = NotificationType((1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 2, 3, 2, 0, 11)).setObjects(("IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: vcModPortInputUtilizationUp.setStatus('current')
vcModPortInputUtilizationDown = NotificationType((1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 2, 3, 2, 0, 12)).setObjects(("IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: vcModPortInputUtilizationDown.setStatus('current')
vcModPortOutputUtilizationUp = NotificationType((1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 2, 3, 2, 0, 13)).setObjects(("IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: vcModPortOutputUtilizationUp.setStatus('current')
vcModPortOutputUtilizationDown = NotificationType((1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 2, 3, 2, 0, 14)).setObjects(("IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: vcModPortOutputUtilizationDown.setStatus('current')
vcModPortInputErrorsUp = NotificationType((1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 2, 3, 2, 0, 15)).setObjects(("IF-MIB", "ifIndex"), ("IF-MIB", "ifInErrors"))
if mibBuilder.loadTexts: vcModPortInputErrorsUp.setStatus('current')
vcModPortInputErrorsDown = NotificationType((1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 2, 3, 2, 0, 16)).setObjects(("IF-MIB", "ifIndex"), ("IF-MIB", "ifInErrors"))
if mibBuilder.loadTexts: vcModPortInputErrorsDown.setStatus('current')
vcModPortOutputErrorsUp = NotificationType((1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 2, 3, 2, 0, 17)).setObjects(("IF-MIB", "ifIndex"), ("IF-MIB", "ifOutErrors"))
if mibBuilder.loadTexts: vcModPortOutputErrorsUp.setStatus('current')
vcModPortOutputErrorsDown = NotificationType((1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 2, 3, 2, 0, 18)).setObjects(("IF-MIB", "ifIndex"), ("IF-MIB", "ifOutErrors"))
if mibBuilder.loadTexts: vcModPortOutputErrorsDown.setStatus('current')
vcModuleMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 2, 3, 3))
vcModuleMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 2, 3, 3, 1))
vcModuleMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 2, 3, 3, 2))
vcModuleMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 2, 3, 3, 1, 1)).setObjects(("HPVCMODULE-MIB", "vcModuleGroup"), ("HPVCMODULE-MIB", "vcModPortThresholdNotificationsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vcModuleMIBCompliance = vcModuleMIBCompliance.setStatus('current')
vcModuleGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 2, 3, 3, 2, 1)).setObjects(("HPVCMODULE-MIB", "vcModuleDomainName"), ("HPVCMODULE-MIB", "vcModuleRole"), ("HPVCMODULE-MIB", "vcModuleDomainPrimaryAddressType"), ("HPVCMODULE-MIB", "vcModuleDomainPrimaryAddress"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vcModuleGroup = vcModuleGroup.setStatus('current')
vcModPortThresholdNotificationsGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 2, 3, 3, 2, 2)).setObjects(("HPVCMODULE-MIB", "vcModPortInputUtilizationUp"), ("HPVCMODULE-MIB", "vcModPortInputUtilizationDown"), ("HPVCMODULE-MIB", "vcModPortOutputUtilizationUp"), ("HPVCMODULE-MIB", "vcModPortOutputUtilizationDown"), ("HPVCMODULE-MIB", "vcModPortInputErrorsUp"), ("HPVCMODULE-MIB", "vcModPortInputErrorsDown"), ("HPVCMODULE-MIB", "vcModPortOutputErrorsUp"), ("HPVCMODULE-MIB", "vcModPortOutputErrorsDown"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vcModPortThresholdNotificationsGroup = vcModPortThresholdNotificationsGroup.setStatus('current')
mibBuilder.exportSymbols("HPVCMODULE-MIB", vcModuleDomainPrimaryAddressType=vcModuleDomainPrimaryAddressType, vcModuleMIBNotificationObjects=vcModuleMIBNotificationObjects, vcModPortOutputUtilizationDown=vcModPortOutputUtilizationDown, vcModuleMIBCompliance=vcModuleMIBCompliance, hpSysMgt=hpSysMgt, vcModPortOutputUtilizationUp=vcModPortOutputUtilizationUp, vcModuleMIB=vcModuleMIB, hp=hp, vcModuleMIBCompliances=vcModuleMIBCompliances, vcModuleDomainName=vcModuleDomainName, virtualConnect=virtualConnect, vcModuleObjects=vcModuleObjects, vcModPortInputErrorsDown=vcModPortInputErrorsDown, vcModuleEnclosureRole=vcModuleEnclosureRole, hpEmbeddedServerMgt=hpEmbeddedServerMgt, vcModPortThresholdNotificationsGroup=vcModPortThresholdNotificationsGroup, vcModuleRole=vcModuleRole, vcModPortOutputErrorsUp=vcModPortOutputErrorsUp, vcModPortInputErrorsUp=vcModPortInputErrorsUp, vcModuleMIBNotifications=vcModuleMIBNotifications, vcModuleMIBNotificationPrefix=vcModuleMIBNotificationPrefix, vcModuleGroup=vcModuleGroup, vcModPortOutputErrorsDown=vcModPortOutputErrorsDown, PYSNMP_MODULE_ID=vcModuleMIB, hpModuleMgmtProc=hpModuleMgmtProc, VcModuleType=VcModuleType, vcModuleDomainPrimaryAddress=vcModuleDomainPrimaryAddress, VcModuleRole=VcModuleRole, vcModPortInputUtilizationDown=vcModPortInputUtilizationDown, vcModuleMIBObjects=vcModuleMIBObjects, vcModPortInputUtilizationUp=vcModPortInputUtilizationUp, vcModuleMIBGroups=vcModuleMIBGroups, vcModuleDomainRoleChange=vcModuleDomainRoleChange, vcModuleMIBConformance=vcModuleMIBConformance, VcEnclosureRole=VcEnclosureRole)
