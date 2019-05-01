#
# PySNMP MIB module HPVCMODULE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HPVCMODULE-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:42:34 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint")
ifOutErrors, ifIndex, ifInErrors = mibBuilder.importSymbols("IF-MIB", "ifOutErrors", "ifIndex", "ifInErrors")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibScalar, MibTable, MibTableRow, MibTableColumn, enterprises, zeroDotZero, Bits, Unsigned32, mib_2, MibIdentifier, IpAddress, TimeTicks, ObjectIdentity, iso, Gauge32, Counter32, Integer32, NotificationType, Counter64, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "enterprises", "zeroDotZero", "Bits", "Unsigned32", "mib-2", "MibIdentifier", "IpAddress", "TimeTicks", "ObjectIdentity", "iso", "Gauge32", "Counter32", "Integer32", "NotificationType", "Counter64", "ModuleIdentity")
RowPointer, TruthValue, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "RowPointer", "TruthValue", "TextualConvention", "DisplayString")
TransportAddressType, TransportAddress = mibBuilder.importSymbols("TRANSPORT-ADDRESS-MIB", "TransportAddressType", "TransportAddress")
hp = MibIdentifier((1, 3, 6, 1, 4, 1, 11))
hpSysMgt = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 5))
hpEmbeddedServerMgt = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 5, 7))
hpModuleMgmtProc = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 5, 7, 5))
virtualConnect = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 2))
vcModuleMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 2, 3))
vcModuleMIB.setRevisions(('2008-10-08 00:00', '2009-02-18 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: vcModuleMIB.setRevisionsDescriptions(('Draft-0. Initial cut. -Jitendra Vegiraju', 'Draft-1. Adding enclosure role object. -Jitendra Vegiraju',))
if mibBuilder.loadTexts: vcModuleMIB.setLastUpdated('200809160000Z')
if mibBuilder.loadTexts: vcModuleMIB.setOrganization('Hewlett-Packard Company')
if mibBuilder.loadTexts: vcModuleMIB.setContactInfo('Robert Teisberg Hewlett-Packard Company. Email: robert.teisberg@hp.com')
if mibBuilder.loadTexts: vcModuleMIB.setDescription('This MIB module describes module specific MIB objects present in each of the Virtual Connect Ethernet (VC-Enet) Modules. These objects represent information about individual VC-Enet modules irrespective of its VC domain role.')
vcModuleMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 2, 3, 1))
vcModuleObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 2, 3, 1, 1))
class VcModuleRole(TextualConvention, Integer32):
    description = 'The virtual connect operational role of this module. The enumerations are described below: unintegrated - module is not a member of a domain primaryProtected - module is VCM primary, and a VCM standby exists primaryUnprotected - module is VCM primary, and no VCM standby exists standby - module is VCM standby other - module is not able to host VCM '
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("unintegrated", 1), ("primaryProtected", 2), ("primaryUnprotected", 3), ("standby", 4), ("other", 5))

class VcEnclosureRole(TextualConvention, Integer32):
    description = 'The virtual connect operational role of the enclosure associated with with this module. The enumerations are described below: unknown - The enclosure role is unknown because of one of the following reasons, - The enclsoure is not part of a VC domain. - The module is in a transitory state. primary - The module is installed in the primary or sole enclosure. secondary - The module is installed in a secondary enclosure of a multi-enclosure domain. '
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("unknown", 1), ("primary", 2), ("secondary", 3))

class VcModuleType(TextualConvention, Integer32):
    description = 'The virtual connect interconnect module type. The enumerations are described below: vcModuleEnet - VC-Enet module vcModuleFC - VC-FC module vcModuleOther - Unknown module or a module not suppported by VC '
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("vcModuleEnet", 1), ("vcModuleFC", 2), ("vcModuleOther", 3))

vcModuleDomainName = MibScalar((1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 2, 3, 1, 1, 1), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vcModuleDomainName.setStatus('current')
if mibBuilder.loadTexts: vcModuleDomainName.setDescription('The administratively assigned name of the Virtual Connect Domain associated with this module.')
vcModuleRole = MibScalar((1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 2, 3, 1, 1, 2), VcModuleRole()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vcModuleRole.setStatus('current')
if mibBuilder.loadTexts: vcModuleRole.setDescription('The VC domain role of this VC module.')
vcModuleDomainPrimaryAddressType = MibScalar((1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 2, 3, 1, 1, 3), TransportAddressType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vcModuleDomainPrimaryAddressType.setStatus('current')
if mibBuilder.loadTexts: vcModuleDomainPrimaryAddressType.setDescription('The transport address type used to address the primary VC module.')
vcModuleDomainPrimaryAddress = MibScalar((1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 2, 3, 1, 1, 4), TransportAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vcModuleDomainPrimaryAddress.setStatus('current')
if mibBuilder.loadTexts: vcModuleDomainPrimaryAddress.setDescription('The address of the primary VC module. The address format is determined by the vcDomainPrimaryAddressType object.')
vcModuleEnclosureRole = MibScalar((1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 2, 3, 1, 1, 5), VcEnclosureRole()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vcModuleEnclosureRole.setStatus('current')
if mibBuilder.loadTexts: vcModuleEnclosureRole.setDescription('The VC enclosure role of the enclosure VC module.')
vcModuleMIBNotificationPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 2, 3, 2))
vcModuleMIBNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 2, 3, 2, 0))
vcModuleMIBNotificationObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 2, 3, 2, 1))
vcModuleDomainRoleChange = NotificationType((1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 2, 3, 2, 0, 1)).setObjects(("HPVCMODULE-MIB", "vcModuleRole"))
if mibBuilder.loadTexts: vcModuleDomainRoleChange.setStatus('current')
if mibBuilder.loadTexts: vcModuleDomainRoleChange.setDescription('The VCM role of the VC module has changed.')
vcModPortInputUtilizationUp = NotificationType((1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 2, 3, 2, 0, 11)).setObjects(("IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: vcModPortInputUtilizationUp.setStatus('current')
if mibBuilder.loadTexts: vcModPortInputUtilizationUp.setDescription('The port input utilization rate has exceeded high threshold. The input line utilization on a port has exceeded its threshold for longer than the threshold averaging period. The ifIndex is the index of the affected port in ifTable.')
vcModPortInputUtilizationDown = NotificationType((1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 2, 3, 2, 0, 12)).setObjects(("IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: vcModPortInputUtilizationDown.setStatus('current')
if mibBuilder.loadTexts: vcModPortInputUtilizationDown.setDescription('The port input utilization rate has dropped below low watermark. The input line utilization on a port has dropped below its low watermark for longer than the threshold averaging period. The ifIndex is the index of the affected port in ifTable.')
vcModPortOutputUtilizationUp = NotificationType((1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 2, 3, 2, 0, 13)).setObjects(("IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: vcModPortOutputUtilizationUp.setStatus('current')
if mibBuilder.loadTexts: vcModPortOutputUtilizationUp.setDescription('The port output utilization rate has exceeded high threshold. The output line utilization on a port has exceeded its high watermark for longer than the threshold averaging period. The ifIndex is the index of the affected port in ifTable.')
vcModPortOutputUtilizationDown = NotificationType((1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 2, 3, 2, 0, 14)).setObjects(("IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: vcModPortOutputUtilizationDown.setStatus('current')
if mibBuilder.loadTexts: vcModPortOutputUtilizationDown.setDescription('The port output utilization rate has dropped below low watermark. The output line utilization on a port has dropped below its low watermark for longer than the threshold averaging period. The ifIndex is the index of the affected port in ifTable.')
vcModPortInputErrorsUp = NotificationType((1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 2, 3, 2, 0, 15)).setObjects(("IF-MIB", "ifIndex"), ("IF-MIB", "ifInErrors"))
if mibBuilder.loadTexts: vcModPortInputErrorsUp.setStatus('current')
if mibBuilder.loadTexts: vcModPortInputErrorsUp.setDescription('The input error count on a port has exceeded high watermark. The input error count on a port has exceeded its high watermark for longer than the error averaging period. The port is identified by ifIndex in ifTable.')
vcModPortInputErrorsDown = NotificationType((1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 2, 3, 2, 0, 16)).setObjects(("IF-MIB", "ifIndex"), ("IF-MIB", "ifInErrors"))
if mibBuilder.loadTexts: vcModPortInputErrorsDown.setStatus('current')
if mibBuilder.loadTexts: vcModPortInputErrorsDown.setDescription('The input error count on a port has dropped below low watermark. The input error count on a port has dropped below its low watermark for longer than the error averaging period. The port is identified by ifIndex in ifTable.')
vcModPortOutputErrorsUp = NotificationType((1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 2, 3, 2, 0, 17)).setObjects(("IF-MIB", "ifIndex"), ("IF-MIB", "ifOutErrors"))
if mibBuilder.loadTexts: vcModPortOutputErrorsUp.setStatus('current')
if mibBuilder.loadTexts: vcModPortOutputErrorsUp.setDescription('The output error count on a port has exceeded its high watermark. The output error count on a port has exceeded its high watermark for longer than the error averaging period. The port is identified by ifIndex in ifTable.')
vcModPortOutputErrorsDown = NotificationType((1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 2, 3, 2, 0, 18)).setObjects(("IF-MIB", "ifIndex"), ("IF-MIB", "ifOutErrors"))
if mibBuilder.loadTexts: vcModPortOutputErrorsDown.setStatus('current')
if mibBuilder.loadTexts: vcModPortOutputErrorsDown.setDescription('The output error count on a port has dropped below its low watermark. The output error count on a port has dropped below its low watermark for longer than the error averaging period. The port is identified by ifIndex in ifTable.')
vcModuleMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 2, 3, 3))
vcModuleMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 2, 3, 3, 1))
vcModuleMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 2, 3, 3, 2))
vcModuleMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 2, 3, 3, 1, 1)).setObjects(("HPVCMODULE-MIB", "vcModuleGroup"), ("HPVCMODULE-MIB", "vcModPortThresholdNotificationsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vcModuleMIBCompliance = vcModuleMIBCompliance.setStatus('current')
if mibBuilder.loadTexts: vcModuleMIBCompliance.setDescription('The compliance statement for entities which implement the VC MIB.')
vcModuleGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 2, 3, 3, 2, 1)).setObjects(("HPVCMODULE-MIB", "vcModuleDomainName"), ("HPVCMODULE-MIB", "vcModuleRole"), ("HPVCMODULE-MIB", "vcModuleDomainPrimaryAddressType"), ("HPVCMODULE-MIB", "vcModuleDomainPrimaryAddress"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vcModuleGroup = vcModuleGroup.setStatus('current')
if mibBuilder.loadTexts: vcModuleGroup.setDescription('Virtual Connect Module objects.')
vcModPortThresholdNotificationsGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 2, 3, 3, 2, 2)).setObjects(("HPVCMODULE-MIB", "vcModPortInputUtilizationUp"), ("HPVCMODULE-MIB", "vcModPortInputUtilizationDown"), ("HPVCMODULE-MIB", "vcModPortOutputUtilizationUp"), ("HPVCMODULE-MIB", "vcModPortOutputUtilizationDown"), ("HPVCMODULE-MIB", "vcModPortInputErrorsUp"), ("HPVCMODULE-MIB", "vcModPortInputErrorsDown"), ("HPVCMODULE-MIB", "vcModPortOutputErrorsUp"), ("HPVCMODULE-MIB", "vcModPortOutputErrorsDown"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vcModPortThresholdNotificationsGroup = vcModPortThresholdNotificationsGroup.setStatus('current')
if mibBuilder.loadTexts: vcModPortThresholdNotificationsGroup.setDescription('The notifications which indicate specific changes in the Virtual Connect port status.')
mibBuilder.exportSymbols("HPVCMODULE-MIB", VcModuleRole=VcModuleRole, vcModuleEnclosureRole=vcModuleEnclosureRole, vcModPortOutputUtilizationUp=vcModPortOutputUtilizationUp, vcModuleDomainPrimaryAddress=vcModuleDomainPrimaryAddress, vcModPortInputErrorsUp=vcModPortInputErrorsUp, hpEmbeddedServerMgt=hpEmbeddedServerMgt, vcModuleMIB=vcModuleMIB, vcModuleMIBGroups=vcModuleMIBGroups, vcModPortInputUtilizationUp=vcModPortInputUtilizationUp, vcModuleDomainPrimaryAddressType=vcModuleDomainPrimaryAddressType, vcModuleMIBObjects=vcModuleMIBObjects, vcModuleMIBNotificationObjects=vcModuleMIBNotificationObjects, hpSysMgt=hpSysMgt, vcModuleRole=vcModuleRole, VcEnclosureRole=VcEnclosureRole, vcModPortInputErrorsDown=vcModPortInputErrorsDown, vcModPortOutputErrorsDown=vcModPortOutputErrorsDown, hp=hp, vcModuleDomainRoleChange=vcModuleDomainRoleChange, vcModuleMIBCompliance=vcModuleMIBCompliance, vcModuleDomainName=vcModuleDomainName, VcModuleType=VcModuleType, vcModPortOutputErrorsUp=vcModPortOutputErrorsUp, vcModuleGroup=vcModuleGroup, vcModuleObjects=vcModuleObjects, vcModuleMIBNotifications=vcModuleMIBNotifications, vcModuleMIBNotificationPrefix=vcModuleMIBNotificationPrefix, vcModuleMIBCompliances=vcModuleMIBCompliances, virtualConnect=virtualConnect, vcModPortInputUtilizationDown=vcModPortInputUtilizationDown, hpModuleMgmtProc=hpModuleMgmtProc, PYSNMP_MODULE_ID=vcModuleMIB, vcModPortOutputUtilizationDown=vcModPortOutputUtilizationDown, vcModPortThresholdNotificationsGroup=vcModPortThresholdNotificationsGroup, vcModuleMIBConformance=vcModuleMIBConformance)
