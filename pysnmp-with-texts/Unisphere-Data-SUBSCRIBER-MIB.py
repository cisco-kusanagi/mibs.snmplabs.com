#
# PySNMP MIB module Unisphere-Data-SUBSCRIBER-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Unisphere-Data-SUBSCRIBER-MIB
# Produced by pysmi-0.3.4 at Wed May  1 15:33:04 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
ObjectIdentity, NotificationType, Counter32, Integer32, IpAddress, Gauge32, iso, ModuleIdentity, Counter64, TimeTicks, Unsigned32, Bits, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "NotificationType", "Counter32", "Integer32", "IpAddress", "Gauge32", "iso", "ModuleIdentity", "Counter64", "TimeTicks", "Unsigned32", "Bits", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
usDataMibs, = mibBuilder.importSymbols("Unisphere-Data-MIBs", "usDataMibs")
UsdEnable, = mibBuilder.importSymbols("Unisphere-Data-TC", "UsdEnable")
usdSubscriberMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 4874, 2, 2, 49))
usdSubscriberMIB.setRevisions(('2002-05-10 19:53', '2000-11-16 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: usdSubscriberMIB.setRevisionsDescriptions(('Added local authentication support.', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: usdSubscriberMIB.setLastUpdated('200205101953Z')
if mibBuilder.loadTexts: usdSubscriberMIB.setOrganization('Unisphere Networks, Inc.')
if mibBuilder.loadTexts: usdSubscriberMIB.setContactInfo(' Unisphere Networks, Inc. Postal: 10 Technology Park Drive Westford, MA 01886 USA Tel: +1 978 589 5800 Email: mib@UnisphereNetworks.com')
if mibBuilder.loadTexts: usdSubscriberMIB.setDescription('The Subscriber MIB for the Unisphere Networks enterprise.')
class UsdSubscrEncaps(TextualConvention, Integer32):
    description = 'Encapsulated protocol type.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 19))
    namedValues = NamedValues(("ip", 0), ("bridgedEthernet", 19))

usdSubscrObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 49, 1))
usdSubscrLocal = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 49, 1, 1))
usdSubscrLocalTable = MibTable((1, 3, 6, 1, 4, 1, 4874, 2, 2, 49, 1, 1, 1), )
if mibBuilder.loadTexts: usdSubscrLocalTable.setStatus('current')
if mibBuilder.loadTexts: usdSubscrLocalTable.setDescription("Permits local configuration associating a remote subscriber's identity with a local interface, for use in circumstances where the remote subscriber's identity cannot be queried directly (e.g. dynamic IPoA operation).")
usdSubscrLocalEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4874, 2, 2, 49, 1, 1, 1, 1), ).setIndexNames((0, "Unisphere-Data-SUBSCRIBER-MIB", "usdSubscrLocalIfIndex"), (0, "Unisphere-Data-SUBSCRIBER-MIB", "usdSubscrLocalEncaps"))
if mibBuilder.loadTexts: usdSubscrLocalEntry.setStatus('current')
if mibBuilder.loadTexts: usdSubscrLocalEntry.setDescription("Local configuration associating a remote subscriber's identity with a local interface.")
usdSubscrLocalIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 49, 1, 1, 1, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: usdSubscrLocalIfIndex.setStatus('current')
if mibBuilder.loadTexts: usdSubscrLocalIfIndex.setDescription('The ifIndex of the interface to which this subscriber information applies.')
usdSubscrLocalEncaps = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 49, 1, 1, 1, 1, 2), UsdSubscrEncaps())
if mibBuilder.loadTexts: usdSubscrLocalEncaps.setStatus('current')
if mibBuilder.loadTexts: usdSubscrLocalEncaps.setDescription('The incoming data encapsulation to which this subscriber information applies. An interface may have a unique subscriber identity configured for each incoming data encapsulation it supports.')
usdSubscrLocalControl = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 49, 1, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("ok", 0), ("clear", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: usdSubscrLocalControl.setStatus('current')
if mibBuilder.loadTexts: usdSubscrLocalControl.setDescription('When set to clear(1), causes the subscriber information in this entry to be cleared. When set to ok(0), there is no effect and subscriber information is unchanged. When read, always returns a value of ok(0). No other object in this entry can be set simultaneously, otherwise an InconsistentValue error is reported.')
usdSubscrLocalNamePrefix = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 49, 1, 1, 1, 1, 4), UsdEnable()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: usdSubscrLocalNamePrefix.setStatus('current')
if mibBuilder.loadTexts: usdSubscrLocalNamePrefix.setDescription('If enabled, indicates whether the value of usdSubscrLocalName is a prefix rather than a full name.')
usdSubscrLocalName = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 49, 1, 1, 1, 1, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 31))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: usdSubscrLocalName.setStatus('current')
if mibBuilder.loadTexts: usdSubscrLocalName.setDescription("The subscriber's name. If usdSubscrLocalNamePrefix has the value 'enabled', the value of this object serves as the prefix of a full subscriber name. The full name is constructed by appending local geographic information (slot, port, etc.) that uniquely distinguishes the subscriber.")
usdSubscrLocalPasswordPrefix = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 49, 1, 1, 1, 1, 6), UsdEnable()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: usdSubscrLocalPasswordPrefix.setStatus('current')
if mibBuilder.loadTexts: usdSubscrLocalPasswordPrefix.setDescription('If enabled, indicates whether the value of usdSubscrLocalPassword prefix rather than a full password.')
usdSubscrLocalPassword = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 49, 1, 1, 1, 1, 7), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 31))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: usdSubscrLocalPassword.setStatus('current')
if mibBuilder.loadTexts: usdSubscrLocalPassword.setDescription("The subscriber's password. If usdSubscrLocalPasswordPrefix has the value 'enabled', the value of this object serves as the prefix of a full subscriber password. The full password is constructed by appending local geographic information (slot, port, etc.) that uniquely distinguishes the subscriber.")
usdSubscrLocalDomain = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 49, 1, 1, 1, 1, 8), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 31))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: usdSubscrLocalDomain.setStatus('current')
if mibBuilder.loadTexts: usdSubscrLocalDomain.setDescription("The subscriber's domain.")
usdSubscrLocalAuthentication = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 49, 1, 1, 1, 1, 9), UsdEnable().clone('enable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: usdSubscrLocalAuthentication.setStatus('current')
if mibBuilder.loadTexts: usdSubscrLocalAuthentication.setDescription('When enabled, the interface performs authentication with RADIUS server using the configured subscriber information and associated with the incoming data encapsulation (usdSubscriberLocalEncaps).')
usdSubscriberMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 49, 4))
usdSubscriberMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 49, 4, 1))
usdSubscriberMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 49, 4, 2))
usdSubscriberCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 4874, 2, 2, 49, 4, 1, 1)).setObjects(("Unisphere-Data-SUBSCRIBER-MIB", "usdSubscriberLocalGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdSubscriberCompliance = usdSubscriberCompliance.setStatus('obsolete')
if mibBuilder.loadTexts: usdSubscriberCompliance.setDescription('Obsolete compliance statement for systems supporting subscriber operation. This statement became obsolete when local authentication support was added.')
usdSubscriberCompliance2 = ModuleCompliance((1, 3, 6, 1, 4, 1, 4874, 2, 2, 49, 4, 1, 2)).setObjects(("Unisphere-Data-SUBSCRIBER-MIB", "usdSubscriberLocalGroup2"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdSubscriberCompliance2 = usdSubscriberCompliance2.setStatus('current')
if mibBuilder.loadTexts: usdSubscriberCompliance2.setDescription('The compliance statement for systems supporting subscriber operation.')
usdSubscriberLocalGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 4874, 2, 2, 49, 4, 2, 1)).setObjects(("Unisphere-Data-SUBSCRIBER-MIB", "usdSubscrLocalControl"), ("Unisphere-Data-SUBSCRIBER-MIB", "usdSubscrLocalNamePrefix"), ("Unisphere-Data-SUBSCRIBER-MIB", "usdSubscrLocalName"), ("Unisphere-Data-SUBSCRIBER-MIB", "usdSubscrLocalPasswordPrefix"), ("Unisphere-Data-SUBSCRIBER-MIB", "usdSubscrLocalPassword"), ("Unisphere-Data-SUBSCRIBER-MIB", "usdSubscrLocalDomain"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdSubscriberLocalGroup = usdSubscriberLocalGroup.setStatus('obsolete')
if mibBuilder.loadTexts: usdSubscriberLocalGroup.setDescription('Obsolete basic collection of objects providing management of locally-configured subscriber identities in a Unisphere product. This group became obsolete when local authentication support was added.')
usdSubscriberLocalGroup2 = ObjectGroup((1, 3, 6, 1, 4, 1, 4874, 2, 2, 49, 4, 2, 2)).setObjects(("Unisphere-Data-SUBSCRIBER-MIB", "usdSubscrLocalControl"), ("Unisphere-Data-SUBSCRIBER-MIB", "usdSubscrLocalNamePrefix"), ("Unisphere-Data-SUBSCRIBER-MIB", "usdSubscrLocalName"), ("Unisphere-Data-SUBSCRIBER-MIB", "usdSubscrLocalPasswordPrefix"), ("Unisphere-Data-SUBSCRIBER-MIB", "usdSubscrLocalPassword"), ("Unisphere-Data-SUBSCRIBER-MIB", "usdSubscrLocalDomain"), ("Unisphere-Data-SUBSCRIBER-MIB", "usdSubscrLocalAuthentication"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdSubscriberLocalGroup2 = usdSubscriberLocalGroup2.setStatus('current')
if mibBuilder.loadTexts: usdSubscriberLocalGroup2.setDescription('The basic collection of objects providing management of locally-configured subscriber identities in a Unisphere product.')
mibBuilder.exportSymbols("Unisphere-Data-SUBSCRIBER-MIB", usdSubscrLocalNamePrefix=usdSubscrLocalNamePrefix, usdSubscrLocalEncaps=usdSubscrLocalEncaps, usdSubscrLocalName=usdSubscrLocalName, usdSubscriberMIBCompliances=usdSubscriberMIBCompliances, usdSubscriberCompliance=usdSubscriberCompliance, usdSubscriberLocalGroup2=usdSubscriberLocalGroup2, usdSubscrLocalEntry=usdSubscrLocalEntry, PYSNMP_MODULE_ID=usdSubscriberMIB, usdSubscrObjects=usdSubscrObjects, usdSubscrLocalPassword=usdSubscrLocalPassword, usdSubscrLocalAuthentication=usdSubscrLocalAuthentication, usdSubscrLocal=usdSubscrLocal, usdSubscrLocalIfIndex=usdSubscrLocalIfIndex, usdSubscriberMIB=usdSubscriberMIB, usdSubscrLocalTable=usdSubscrLocalTable, usdSubscriberMIBConformance=usdSubscriberMIBConformance, usdSubscrLocalControl=usdSubscrLocalControl, UsdSubscrEncaps=UsdSubscrEncaps, usdSubscriberMIBGroups=usdSubscriberMIBGroups, usdSubscrLocalDomain=usdSubscrLocalDomain, usdSubscriberLocalGroup=usdSubscriberLocalGroup, usdSubscriberCompliance2=usdSubscriberCompliance2, usdSubscrLocalPasswordPrefix=usdSubscrLocalPasswordPrefix)
