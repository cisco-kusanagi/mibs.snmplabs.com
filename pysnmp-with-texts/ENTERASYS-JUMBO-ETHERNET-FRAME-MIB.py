#
# PySNMP MIB module ENTERASYS-JUMBO-ETHERNET-FRAME-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ENTERASYS-JUMBO-ETHERNET-FRAME-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:03:44 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion")
etsysModules, = mibBuilder.importSymbols("ENTERASYS-MIB-NAMES", "etsysModules")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
EnabledStatus, = mibBuilder.importSymbols("P-BRIDGE-MIB", "EnabledStatus")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
ObjectIdentity, iso, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, Gauge32, Counter32, Bits, Counter64, IpAddress, NotificationType, MibIdentifier, ModuleIdentity, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "iso", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "Gauge32", "Counter32", "Bits", "Counter64", "IpAddress", "NotificationType", "MibIdentifier", "ModuleIdentity", "TimeTicks")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
etsysJumboEthernetFrameMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 5624, 1, 2, 34))
etsysJumboEthernetFrameMIB.setRevisions(('2003-01-24 21:26', '2002-12-20 21:56',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: etsysJumboEthernetFrameMIB.setRevisionsDescriptions(('Changed the per port enable status to a per port administrative and operational status.', 'The initial version of this MIB module',))
if mibBuilder.loadTexts: etsysJumboEthernetFrameMIB.setLastUpdated('200301242126Z')
if mibBuilder.loadTexts: etsysJumboEthernetFrameMIB.setOrganization('Enterasys Networks, Inc')
if mibBuilder.loadTexts: etsysJumboEthernetFrameMIB.setContactInfo('Postal: Enterasys Networks 35 Industrial Way, P.O. Box 5005 Rochester, NH 03867-0505 Phone: +1 603 332 9400 E-mail: support@enterasys.com WWW: http://www.enterasys.com')
if mibBuilder.loadTexts: etsysJumboEthernetFrameMIB.setDescription('This MIB module defines a portion of the SNMP MIB under the Enterasys Networks enterprise OID pertaining to jumbo Ethernet frames.')
etsysJumboEthernetFrame = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 34, 1))
etsysJumboEnetFrameControl = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 34, 1, 1))
etsysJumboEnetFrameTable = MibTable((1, 3, 6, 1, 4, 1, 5624, 1, 2, 34, 1, 1, 1), )
if mibBuilder.loadTexts: etsysJumboEnetFrameTable.setStatus('current')
if mibBuilder.loadTexts: etsysJumboEnetFrameTable.setDescription('A list of entries for interfaces that have support for jumbo Ethernet frames.')
etsysJumboEnetFrameEntry = MibTableRow((1, 3, 6, 1, 4, 1, 5624, 1, 2, 34, 1, 1, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: etsysJumboEnetFrameEntry.setStatus('current')
if mibBuilder.loadTexts: etsysJumboEnetFrameEntry.setDescription('An entry containing management information applicable to a particular interface that has support for jumbo Ethernet frames.')
etsysJumboEnetFrameEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 34, 1, 1, 1, 1, 1), EnabledStatus().clone('disabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: etsysJumboEnetFrameEnable.setStatus('obsolete')
if mibBuilder.loadTexts: etsysJumboEnetFrameEnable.setDescription('The enabled/disabled status of the passing of jumbo Ethernet frames on the interface.')
etsysJumboEnetFrameMtu = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 34, 1, 1, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: etsysJumboEnetFrameMtu.setReference('IETF RFC2863 IF-MIB')
if mibBuilder.loadTexts: etsysJumboEnetFrameMtu.setStatus('current')
if mibBuilder.loadTexts: etsysJumboEnetFrameMtu.setDescription('The MTU for this interface when etsysJumboEnetFrameEnable is enabled. The managed entity will reflect this value in ifMtu when the passing of jumbo frames is enabled on this interface.')
etsysJumboEnetFrameAdminStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 34, 1, 1, 1, 1, 3), EnabledStatus().clone('disabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: etsysJumboEnetFrameAdminStatus.setStatus('current')
if mibBuilder.loadTexts: etsysJumboEnetFrameAdminStatus.setDescription('The administrative enabled/disabled status for the passing of jumbo Ethernet frames on this interface.')
etsysJumboEnetFrameOperStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 34, 1, 1, 1, 1, 4), EnabledStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: etsysJumboEnetFrameOperStatus.setStatus('current')
if mibBuilder.loadTexts: etsysJumboEnetFrameOperStatus.setDescription('The operational status of the passing of jumbo Ethernet frames on this interface.')
etsysJumboEnetFrameConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 34, 2))
etsysJumboEnetFrameGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 34, 2, 1))
etsysJumboEnetFrameCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 34, 2, 2))
etsysJumboEnetFrameControlGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 5624, 1, 2, 34, 2, 1, 1)).setObjects(("ENTERASYS-JUMBO-ETHERNET-FRAME-MIB", "etsysJumboEnetFrameEnable"), ("ENTERASYS-JUMBO-ETHERNET-FRAME-MIB", "etsysJumboEnetFrameMtu"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    etsysJumboEnetFrameControlGroup = etsysJumboEnetFrameControlGroup.setStatus('obsolete')
if mibBuilder.loadTexts: etsysJumboEnetFrameControlGroup.setDescription('A collection of objects relating to per interface Jumbo Ethernet frame support.')
etsysJumboEnetFrameControlGroup2 = ObjectGroup((1, 3, 6, 1, 4, 1, 5624, 1, 2, 34, 2, 1, 2)).setObjects(("ENTERASYS-JUMBO-ETHERNET-FRAME-MIB", "etsysJumboEnetFrameMtu"), ("ENTERASYS-JUMBO-ETHERNET-FRAME-MIB", "etsysJumboEnetFrameAdminStatus"), ("ENTERASYS-JUMBO-ETHERNET-FRAME-MIB", "etsysJumboEnetFrameOperStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    etsysJumboEnetFrameControlGroup2 = etsysJumboEnetFrameControlGroup2.setStatus('current')
if mibBuilder.loadTexts: etsysJumboEnetFrameControlGroup2.setDescription('A collection of objects relating to per interface Jumbo Ethernet frame support.')
etsysJumboEnetFrameCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 5624, 1, 2, 34, 2, 2, 1)).setObjects(("ENTERASYS-JUMBO-ETHERNET-FRAME-MIB", "etsysJumboEnetFrameControlGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    etsysJumboEnetFrameCompliance = etsysJumboEnetFrameCompliance.setStatus('obsolete')
if mibBuilder.loadTexts: etsysJumboEnetFrameCompliance.setDescription('The compliance statement for devices that support the Enterasys Jumbo Ethernet Frame MIB.')
etsysJumboEnetFrameCompliance2 = ModuleCompliance((1, 3, 6, 1, 4, 1, 5624, 1, 2, 34, 2, 2, 2)).setObjects(("ENTERASYS-JUMBO-ETHERNET-FRAME-MIB", "etsysJumboEnetFrameControlGroup2"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    etsysJumboEnetFrameCompliance2 = etsysJumboEnetFrameCompliance2.setStatus('current')
if mibBuilder.loadTexts: etsysJumboEnetFrameCompliance2.setDescription('The compliance statement for devices that support the Enterasys Jumbo Ethernet Frame MIB.')
mibBuilder.exportSymbols("ENTERASYS-JUMBO-ETHERNET-FRAME-MIB", etsysJumboEnetFrameCompliances=etsysJumboEnetFrameCompliances, etsysJumboEnetFrameTable=etsysJumboEnetFrameTable, etsysJumboEnetFrameMtu=etsysJumboEnetFrameMtu, etsysJumboEnetFrameConformance=etsysJumboEnetFrameConformance, etsysJumboEnetFrameControlGroup=etsysJumboEnetFrameControlGroup, etsysJumboEthernetFrameMIB=etsysJumboEthernetFrameMIB, etsysJumboEnetFrameControlGroup2=etsysJumboEnetFrameControlGroup2, etsysJumboEnetFrameCompliance2=etsysJumboEnetFrameCompliance2, etsysJumboEnetFrameEntry=etsysJumboEnetFrameEntry, etsysJumboEnetFrameEnable=etsysJumboEnetFrameEnable, etsysJumboEnetFrameOperStatus=etsysJumboEnetFrameOperStatus, etsysJumboEnetFrameGroups=etsysJumboEnetFrameGroups, etsysJumboEnetFrameControl=etsysJumboEnetFrameControl, etsysJumboEnetFrameCompliance=etsysJumboEnetFrameCompliance, etsysJumboEthernetFrame=etsysJumboEthernetFrame, etsysJumboEnetFrameAdminStatus=etsysJumboEnetFrameAdminStatus, PYSNMP_MODULE_ID=etsysJumboEthernetFrameMIB)
