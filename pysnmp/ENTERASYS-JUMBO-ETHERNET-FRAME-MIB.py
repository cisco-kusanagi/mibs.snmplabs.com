#
# PySNMP MIB module ENTERASYS-JUMBO-ETHERNET-FRAME-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ENTERASYS-JUMBO-ETHERNET-FRAME-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:49:21 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint")
etsysModules, = mibBuilder.importSymbols("ENTERASYS-MIB-NAMES", "etsysModules")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
EnabledStatus, = mibBuilder.importSymbols("P-BRIDGE-MIB", "EnabledStatus")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
Counter64, Unsigned32, Gauge32, ModuleIdentity, iso, NotificationType, ObjectIdentity, TimeTicks, IpAddress, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, Bits, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "Unsigned32", "Gauge32", "ModuleIdentity", "iso", "NotificationType", "ObjectIdentity", "TimeTicks", "IpAddress", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "Bits", "Integer32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
etsysJumboEthernetFrameMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 5624, 1, 2, 34))
etsysJumboEthernetFrameMIB.setRevisions(('2003-01-24 21:26', '2002-12-20 21:56',))
if mibBuilder.loadTexts: etsysJumboEthernetFrameMIB.setLastUpdated('200301242126Z')
if mibBuilder.loadTexts: etsysJumboEthernetFrameMIB.setOrganization('Enterasys Networks, Inc')
etsysJumboEthernetFrame = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 34, 1))
etsysJumboEnetFrameControl = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 34, 1, 1))
etsysJumboEnetFrameTable = MibTable((1, 3, 6, 1, 4, 1, 5624, 1, 2, 34, 1, 1, 1), )
if mibBuilder.loadTexts: etsysJumboEnetFrameTable.setStatus('current')
etsysJumboEnetFrameEntry = MibTableRow((1, 3, 6, 1, 4, 1, 5624, 1, 2, 34, 1, 1, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: etsysJumboEnetFrameEntry.setStatus('current')
etsysJumboEnetFrameEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 34, 1, 1, 1, 1, 1), EnabledStatus().clone('disabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: etsysJumboEnetFrameEnable.setStatus('obsolete')
etsysJumboEnetFrameMtu = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 34, 1, 1, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: etsysJumboEnetFrameMtu.setStatus('current')
etsysJumboEnetFrameAdminStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 34, 1, 1, 1, 1, 3), EnabledStatus().clone('disabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: etsysJumboEnetFrameAdminStatus.setStatus('current')
etsysJumboEnetFrameOperStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 34, 1, 1, 1, 1, 4), EnabledStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: etsysJumboEnetFrameOperStatus.setStatus('current')
etsysJumboEnetFrameConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 34, 2))
etsysJumboEnetFrameGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 34, 2, 1))
etsysJumboEnetFrameCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 34, 2, 2))
etsysJumboEnetFrameControlGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 5624, 1, 2, 34, 2, 1, 1)).setObjects(("ENTERASYS-JUMBO-ETHERNET-FRAME-MIB", "etsysJumboEnetFrameEnable"), ("ENTERASYS-JUMBO-ETHERNET-FRAME-MIB", "etsysJumboEnetFrameMtu"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    etsysJumboEnetFrameControlGroup = etsysJumboEnetFrameControlGroup.setStatus('obsolete')
etsysJumboEnetFrameControlGroup2 = ObjectGroup((1, 3, 6, 1, 4, 1, 5624, 1, 2, 34, 2, 1, 2)).setObjects(("ENTERASYS-JUMBO-ETHERNET-FRAME-MIB", "etsysJumboEnetFrameMtu"), ("ENTERASYS-JUMBO-ETHERNET-FRAME-MIB", "etsysJumboEnetFrameAdminStatus"), ("ENTERASYS-JUMBO-ETHERNET-FRAME-MIB", "etsysJumboEnetFrameOperStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    etsysJumboEnetFrameControlGroup2 = etsysJumboEnetFrameControlGroup2.setStatus('current')
etsysJumboEnetFrameCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 5624, 1, 2, 34, 2, 2, 1)).setObjects(("ENTERASYS-JUMBO-ETHERNET-FRAME-MIB", "etsysJumboEnetFrameControlGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    etsysJumboEnetFrameCompliance = etsysJumboEnetFrameCompliance.setStatus('obsolete')
etsysJumboEnetFrameCompliance2 = ModuleCompliance((1, 3, 6, 1, 4, 1, 5624, 1, 2, 34, 2, 2, 2)).setObjects(("ENTERASYS-JUMBO-ETHERNET-FRAME-MIB", "etsysJumboEnetFrameControlGroup2"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    etsysJumboEnetFrameCompliance2 = etsysJumboEnetFrameCompliance2.setStatus('current')
mibBuilder.exportSymbols("ENTERASYS-JUMBO-ETHERNET-FRAME-MIB", PYSNMP_MODULE_ID=etsysJumboEthernetFrameMIB, etsysJumboEnetFrameControl=etsysJumboEnetFrameControl, etsysJumboEnetFrameTable=etsysJumboEnetFrameTable, etsysJumboEnetFrameMtu=etsysJumboEnetFrameMtu, etsysJumboEnetFrameEnable=etsysJumboEnetFrameEnable, etsysJumboEnetFrameControlGroup=etsysJumboEnetFrameControlGroup, etsysJumboEnetFrameCompliance=etsysJumboEnetFrameCompliance, etsysJumboEnetFrameOperStatus=etsysJumboEnetFrameOperStatus, etsysJumboEnetFrameConformance=etsysJumboEnetFrameConformance, etsysJumboEnetFrameEntry=etsysJumboEnetFrameEntry, etsysJumboEthernetFrame=etsysJumboEthernetFrame, etsysJumboEnetFrameGroups=etsysJumboEnetFrameGroups, etsysJumboEthernetFrameMIB=etsysJumboEthernetFrameMIB, etsysJumboEnetFrameControlGroup2=etsysJumboEnetFrameControlGroup2, etsysJumboEnetFrameAdminStatus=etsysJumboEnetFrameAdminStatus, etsysJumboEnetFrameCompliance2=etsysJumboEnetFrameCompliance2, etsysJumboEnetFrameCompliances=etsysJumboEnetFrameCompliances)
