#
# PySNMP MIB module ENTERASYS-RTR-ADVERT-NOTIFICATION-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ENTERASYS-RTR-ADVERT-NOTIFICATION-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:50:15 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint")
etsysModules, = mibBuilder.importSymbols("ENTERASYS-MIB-NAMES", "etsysModules")
ifName, = mibBuilder.importSymbols("IF-MIB", "ifName")
InetAddress, InetAddressType = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddress", "InetAddressType")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
ModuleIdentity, NotificationType, Gauge32, Counter32, IpAddress, MibIdentifier, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, Integer32, Counter64, iso, Bits, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "NotificationType", "Gauge32", "Counter32", "IpAddress", "MibIdentifier", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "Integer32", "Counter64", "iso", "Bits", "Unsigned32")
TextualConvention, DisplayString, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString", "TruthValue")
etsysRtrAdvertNotificationMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 5624, 1, 2, 82))
etsysRtrAdvertNotificationMIB.setRevisions(('2011-05-13 13:47',))
if mibBuilder.loadTexts: etsysRtrAdvertNotificationMIB.setLastUpdated('201105131347Z')
if mibBuilder.loadTexts: etsysRtrAdvertNotificationMIB.setOrganization('Enterasys Networks, Inc')
etsysRtrAdvertNotificationObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 82, 1))
etsysRtrAdvertConfigBranch = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 82, 1, 0))
etsysRtrAdvertInformationBranch = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 82, 1, 1))
etsysRtrAdvertNotificationBranch = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 82, 1, 2))
etsysRtrAdvertInconsistentEnabled = MibScalar((1, 3, 6, 1, 4, 1, 5624, 1, 2, 82, 1, 0, 1), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: etsysRtrAdvertInconsistentEnabled.setStatus('current')
etsysRtrAdvertInetAddrType = MibScalar((1, 3, 6, 1, 4, 1, 5624, 1, 2, 82, 1, 1, 1), InetAddressType()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: etsysRtrAdvertInetAddrType.setStatus('current')
etsysRtrAdvertInetAddress = MibScalar((1, 3, 6, 1, 4, 1, 5624, 1, 2, 82, 1, 1, 2), InetAddress()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: etsysRtrAdvertInetAddress.setStatus('current')
etsysRtrAdvertUserData = MibScalar((1, 3, 6, 1, 4, 1, 5624, 1, 2, 82, 1, 1, 3), SnmpAdminString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: etsysRtrAdvertUserData.setStatus('current')
etsysRtrAdvertInconsistent = NotificationType((1, 3, 6, 1, 4, 1, 5624, 1, 2, 82, 1, 2, 1)).setObjects(("ENTERASYS-RTR-ADVERT-NOTIFICATION-MIB", "etsysRtrAdvertInetAddrType"), ("ENTERASYS-RTR-ADVERT-NOTIFICATION-MIB", "etsysRtrAdvertInetAddress"), ("IF-MIB", "ifName"), ("ENTERASYS-RTR-ADVERT-NOTIFICATION-MIB", "etsysRtrAdvertUserData"))
if mibBuilder.loadTexts: etsysRtrAdvertInconsistent.setStatus('current')
etsysRtrAdvertConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 82, 2))
etsysRtrAdvertGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 82, 2, 1))
etsysRtrAdvertCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 82, 2, 2))
etsysRtrAdvertConfigGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 5624, 1, 2, 82, 2, 1, 1)).setObjects(("ENTERASYS-RTR-ADVERT-NOTIFICATION-MIB", "etsysRtrAdvertInconsistentEnabled"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    etsysRtrAdvertConfigGroup = etsysRtrAdvertConfigGroup.setStatus('current')
etsysRtrAdvertInformationGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 5624, 1, 2, 82, 2, 1, 2)).setObjects(("ENTERASYS-RTR-ADVERT-NOTIFICATION-MIB", "etsysRtrAdvertInetAddrType"), ("ENTERASYS-RTR-ADVERT-NOTIFICATION-MIB", "etsysRtrAdvertInetAddress"), ("ENTERASYS-RTR-ADVERT-NOTIFICATION-MIB", "etsysRtrAdvertUserData"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    etsysRtrAdvertInformationGroup = etsysRtrAdvertInformationGroup.setStatus('current')
etsysRtrAdvertNotificationGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 5624, 1, 2, 82, 2, 1, 3)).setObjects(("ENTERASYS-RTR-ADVERT-NOTIFICATION-MIB", "etsysRtrAdvertInconsistent"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    etsysRtrAdvertNotificationGroup = etsysRtrAdvertNotificationGroup.setStatus('current')
etsysRtrAdvertCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 5624, 1, 2, 82, 2, 2, 1)).setObjects(("ENTERASYS-RTR-ADVERT-NOTIFICATION-MIB", "etsysRtrAdvertConfigGroup"), ("ENTERASYS-RTR-ADVERT-NOTIFICATION-MIB", "etsysRtrAdvertInformationGroup"), ("ENTERASYS-RTR-ADVERT-NOTIFICATION-MIB", "etsysRtrAdvertNotificationGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    etsysRtrAdvertCompliance = etsysRtrAdvertCompliance.setStatus('current')
mibBuilder.exportSymbols("ENTERASYS-RTR-ADVERT-NOTIFICATION-MIB", etsysRtrAdvertConfigBranch=etsysRtrAdvertConfigBranch, etsysRtrAdvertNotificationMIB=etsysRtrAdvertNotificationMIB, etsysRtrAdvertInformationGroup=etsysRtrAdvertInformationGroup, etsysRtrAdvertNotificationBranch=etsysRtrAdvertNotificationBranch, etsysRtrAdvertInformationBranch=etsysRtrAdvertInformationBranch, PYSNMP_MODULE_ID=etsysRtrAdvertNotificationMIB, etsysRtrAdvertInetAddrType=etsysRtrAdvertInetAddrType, etsysRtrAdvertUserData=etsysRtrAdvertUserData, etsysRtrAdvertInconsistent=etsysRtrAdvertInconsistent, etsysRtrAdvertConformance=etsysRtrAdvertConformance, etsysRtrAdvertCompliances=etsysRtrAdvertCompliances, etsysRtrAdvertConfigGroup=etsysRtrAdvertConfigGroup, etsysRtrAdvertNotificationGroup=etsysRtrAdvertNotificationGroup, etsysRtrAdvertNotificationObjects=etsysRtrAdvertNotificationObjects, etsysRtrAdvertInetAddress=etsysRtrAdvertInetAddress, etsysRtrAdvertGroups=etsysRtrAdvertGroups, etsysRtrAdvertInconsistentEnabled=etsysRtrAdvertInconsistentEnabled, etsysRtrAdvertCompliance=etsysRtrAdvertCompliance)
