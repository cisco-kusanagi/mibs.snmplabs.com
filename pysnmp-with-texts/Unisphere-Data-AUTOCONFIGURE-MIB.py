#
# PySNMP MIB module Unisphere-Data-AUTOCONFIGURE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Unisphere-Data-AUTOCONFIGURE-MIB
# Produced by pysmi-0.3.4 at Wed May  1 15:30:27 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
Counter64, NotificationType, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, TimeTicks, MibIdentifier, Bits, Integer32, iso, Counter32, ModuleIdentity, Unsigned32, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "NotificationType", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "TimeTicks", "MibIdentifier", "Bits", "Integer32", "iso", "Counter32", "ModuleIdentity", "Unsigned32", "Gauge32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
usDataMibs, = mibBuilder.importSymbols("Unisphere-Data-MIBs", "usDataMibs")
UsdEnable, = mibBuilder.importSymbols("Unisphere-Data-TC", "UsdEnable")
usdAutoConfMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 4874, 2, 2, 48))
usdAutoConfMIB.setRevisions(('2002-11-18 00:00', '2000-11-16 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: usdAutoConfMIB.setRevisionsDescriptions(('Added bridgedEthernet(19) to UsdAutoConfEncaps.', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: usdAutoConfMIB.setLastUpdated('200211190000Z')
if mibBuilder.loadTexts: usdAutoConfMIB.setOrganization('Unisphere Networks Inc.')
if mibBuilder.loadTexts: usdAutoConfMIB.setContactInfo(' Unisphere Networks, Inc. Postal: 10 Technology Park Drive Westford MA 01886 USA Tel: +1 978 589 5800 Email: mib@UnisphereNetworks.com')
if mibBuilder.loadTexts: usdAutoConfMIB.setDescription('The Auto-Configuration MIB for the Unisphere Networks Inc. enterprise.')
class UsdAutoConfEncaps(TextualConvention, Integer32):
    description = 'Encapsulated protocol type.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 17, 19))
    namedValues = NamedValues(("ip", 0), ("ppp", 1), ("pppoe", 17), ("bridgedEthernet", 19))

usdAutoConfObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 48, 1))
usdAutoConf = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 48, 1, 1))
usdAutoConfTable = MibTable((1, 3, 6, 1, 4, 1, 4874, 2, 2, 48, 1, 1, 1), )
if mibBuilder.loadTexts: usdAutoConfTable.setStatus('current')
if mibBuilder.loadTexts: usdAutoConfTable.setDescription('Configures recognition of incoming data encapsulation types that trigger autoconfiguration on an interface.')
usdAutoConfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4874, 2, 2, 48, 1, 1, 1, 1), ).setIndexNames((0, "Unisphere-Data-AUTOCONFIGURE-MIB", "usdAutoConfIfIndex"), (0, "Unisphere-Data-AUTOCONFIGURE-MIB", "usdAutoConfEncaps"))
if mibBuilder.loadTexts: usdAutoConfEntry.setStatus('current')
if mibBuilder.loadTexts: usdAutoConfEntry.setDescription('Configures recognition of an incoming data encapsulation type that triggers autoconfiguration on an interface.')
usdAutoConfIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 48, 1, 1, 1, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: usdAutoConfIfIndex.setStatus('current')
if mibBuilder.loadTexts: usdAutoConfIfIndex.setDescription('The ifIndex of the interface to which the autoconfiguration information in this entry applies.')
usdAutoConfEncaps = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 48, 1, 1, 1, 1, 2), UsdAutoConfEncaps())
if mibBuilder.loadTexts: usdAutoConfEncaps.setStatus('current')
if mibBuilder.loadTexts: usdAutoConfEncaps.setDescription('The encapsulated protocol type to which the autconfiguration information in this entry applies.')
usdAutoConfEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 48, 1, 1, 1, 1, 3), UsdEnable()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: usdAutoConfEnable.setStatus('current')
if mibBuilder.loadTexts: usdAutoConfEnable.setDescription('When enabled, permits autoconfiguration of the specified interface when the specified encapsulation is recognized in an incoming data frame.')
usdAutoConfMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 48, 4))
usdAutoConfMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 48, 4, 1))
usdAutoConfMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 48, 4, 2))
usdAutoConfCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 4874, 2, 2, 48, 4, 1, 1)).setObjects(("Unisphere-Data-AUTOCONFIGURE-MIB", "usdAutoConfGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdAutoConfCompliance = usdAutoConfCompliance.setStatus('current')
if mibBuilder.loadTexts: usdAutoConfCompliance.setDescription('The compliance statement for systems supporting enabling of autoconfiguration operation.')
usdAutoConfGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 4874, 2, 2, 48, 4, 2, 1)).setObjects(("Unisphere-Data-AUTOCONFIGURE-MIB", "usdAutoConfEnable"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdAutoConfGroup = usdAutoConfGroup.setStatus('current')
if mibBuilder.loadTexts: usdAutoConfGroup.setDescription('The basic collection of objects providing management of autoconfiguration enabling in a Unisphere product.')
mibBuilder.exportSymbols("Unisphere-Data-AUTOCONFIGURE-MIB", usdAutoConf=usdAutoConf, usdAutoConfIfIndex=usdAutoConfIfIndex, usdAutoConfMIB=usdAutoConfMIB, usdAutoConfEnable=usdAutoConfEnable, usdAutoConfCompliance=usdAutoConfCompliance, usdAutoConfObjects=usdAutoConfObjects, usdAutoConfEncaps=usdAutoConfEncaps, usdAutoConfEntry=usdAutoConfEntry, PYSNMP_MODULE_ID=usdAutoConfMIB, usdAutoConfMIBCompliances=usdAutoConfMIBCompliances, usdAutoConfTable=usdAutoConfTable, UsdAutoConfEncaps=UsdAutoConfEncaps, usdAutoConfGroup=usdAutoConfGroup, usdAutoConfMIBGroups=usdAutoConfMIBGroups, usdAutoConfMIBConformance=usdAutoConfMIBConformance)
