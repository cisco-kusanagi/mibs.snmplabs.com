#
# PySNMP MIB module Juniper-SUBSCRIBER-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/JUNIPER-SUBSCRIBER-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:01:13 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
juniMibs, = mibBuilder.importSymbols("Juniper-MIBs", "juniMibs")
JuniEnable, = mibBuilder.importSymbols("Juniper-TC", "JuniEnable")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
Counter64, NotificationType, Gauge32, IpAddress, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, TimeTicks, ObjectIdentity, Counter32, MibIdentifier, Integer32, Unsigned32, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "NotificationType", "Gauge32", "IpAddress", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "TimeTicks", "ObjectIdentity", "Counter32", "MibIdentifier", "Integer32", "Unsigned32", "Bits")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
juniSubscriberMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 4874, 2, 2, 49))
juniSubscriberMIB.setRevisions(('2002-09-16 21:44', '2002-05-10 19:53', '2000-11-16 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: juniSubscriberMIB.setRevisionsDescriptions(('Replaced Unisphere names with Juniper names.', 'Added local authentication support.', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: juniSubscriberMIB.setLastUpdated('200209162144Z')
if mibBuilder.loadTexts: juniSubscriberMIB.setOrganization('Juniper Networks, Inc.')
if mibBuilder.loadTexts: juniSubscriberMIB.setContactInfo(' Juniper Networks, Inc. Postal: 10 Technology Park Drive Westford, MA 01886-3146 USA Tel: +1 978 589 5800 Email: mib@Juniper.net')
if mibBuilder.loadTexts: juniSubscriberMIB.setDescription('The Subscriber MIB for the Juniper Networks enterprise.')
class JuniSubscrEncaps(TextualConvention, Integer32):
    description = 'Encapsulated protocol type.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 19))
    namedValues = NamedValues(("ip", 0), ("bridgedEthernet", 19))

juniSubscrObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 49, 1))
juniSubscrLocal = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 49, 1, 1))
juniSubscrLocalTable = MibTable((1, 3, 6, 1, 4, 1, 4874, 2, 2, 49, 1, 1, 1), )
if mibBuilder.loadTexts: juniSubscrLocalTable.setStatus('current')
if mibBuilder.loadTexts: juniSubscrLocalTable.setDescription("Permits local configuration associating a remote subscriber's identity with a local interface, for use in circumstances where the remote subscriber's identity cannot be queried directly (e.g. dynamic IPoA operation).")
juniSubscrLocalEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4874, 2, 2, 49, 1, 1, 1, 1), ).setIndexNames((0, "Juniper-SUBSCRIBER-MIB", "juniSubscrLocalIfIndex"), (0, "Juniper-SUBSCRIBER-MIB", "juniSubscrLocalEncaps"))
if mibBuilder.loadTexts: juniSubscrLocalEntry.setStatus('current')
if mibBuilder.loadTexts: juniSubscrLocalEntry.setDescription("Local configuration associating a remote subscriber's identity with a local interface.")
juniSubscrLocalIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 49, 1, 1, 1, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: juniSubscrLocalIfIndex.setStatus('current')
if mibBuilder.loadTexts: juniSubscrLocalIfIndex.setDescription('The ifIndex of the interface to which this subscriber information applies.')
juniSubscrLocalEncaps = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 49, 1, 1, 1, 1, 2), JuniSubscrEncaps())
if mibBuilder.loadTexts: juniSubscrLocalEncaps.setStatus('current')
if mibBuilder.loadTexts: juniSubscrLocalEncaps.setDescription('The incoming data encapsulation to which this subscriber information applies. An interface may have a unique subscriber identity configured for each incoming data encapsulation it supports.')
juniSubscrLocalControl = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 49, 1, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("ok", 0), ("clear", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: juniSubscrLocalControl.setStatus('current')
if mibBuilder.loadTexts: juniSubscrLocalControl.setDescription('When set to clear(1), causes the subscriber information in this entry to be cleared. When set to ok(0), there is no effect and subscriber information is unchanged. When read, always returns a value of ok(0). No other object in this entry can be set simultaneously, otherwise an InconsistentValue error is reported.')
juniSubscrLocalNamePrefix = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 49, 1, 1, 1, 1, 4), JuniEnable()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: juniSubscrLocalNamePrefix.setStatus('current')
if mibBuilder.loadTexts: juniSubscrLocalNamePrefix.setDescription('If enabled, indicates whether the value of juniSubscrLocalName is a prefix rather than a full name.')
juniSubscrLocalName = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 49, 1, 1, 1, 1, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 31))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: juniSubscrLocalName.setStatus('current')
if mibBuilder.loadTexts: juniSubscrLocalName.setDescription("The subscriber's name. If juniSubscrLocalNamePrefix has the value 'enabled', the value of this object serves as the prefix of a full subscriber name. The full name is constructed by appending local geographic information (slot, port, etc.) that uniquely distinguishes the subscriber.")
juniSubscrLocalPasswordPrefix = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 49, 1, 1, 1, 1, 6), JuniEnable()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: juniSubscrLocalPasswordPrefix.setStatus('current')
if mibBuilder.loadTexts: juniSubscrLocalPasswordPrefix.setDescription('If enabled, indicates whether the value of juniSubscrLocalPassword prefix rather than a full password.')
juniSubscrLocalPassword = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 49, 1, 1, 1, 1, 7), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 31))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: juniSubscrLocalPassword.setStatus('current')
if mibBuilder.loadTexts: juniSubscrLocalPassword.setDescription("The subscriber's password. If juniSubscrLocalPasswordPrefix has the value 'enabled', the value of this object serves as the prefix of a full subscriber password. The full password is constructed by appending local geographic information (slot, port, etc.) that uniquely distinguishes the subscriber.")
juniSubscrLocalDomain = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 49, 1, 1, 1, 1, 8), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 31))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: juniSubscrLocalDomain.setStatus('current')
if mibBuilder.loadTexts: juniSubscrLocalDomain.setDescription("The subscriber's domain.")
juniSubscrLocalAuthentication = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 49, 1, 1, 1, 1, 9), JuniEnable().clone('enable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: juniSubscrLocalAuthentication.setStatus('current')
if mibBuilder.loadTexts: juniSubscrLocalAuthentication.setDescription('When enabled, the interface performs authentication with RADIUS server using the configured subscriber information and associated with the incoming data encapsulation (juniSubscriberLocalEncaps).')
juniSubscriberMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 49, 4))
juniSubscriberMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 49, 4, 1))
juniSubscriberMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 49, 4, 2))
juniSubscriberCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 4874, 2, 2, 49, 4, 1, 1)).setObjects(("Juniper-SUBSCRIBER-MIB", "juniSubscriberLocalGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniSubscriberCompliance = juniSubscriberCompliance.setStatus('obsolete')
if mibBuilder.loadTexts: juniSubscriberCompliance.setDescription('Obsolete compliance statement for systems supporting subscriber operation. This statement became obsolete when local authentication support was added.')
juniSubscriberCompliance2 = ModuleCompliance((1, 3, 6, 1, 4, 1, 4874, 2, 2, 49, 4, 1, 2)).setObjects(("Juniper-SUBSCRIBER-MIB", "juniSubscriberLocalGroup2"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniSubscriberCompliance2 = juniSubscriberCompliance2.setStatus('current')
if mibBuilder.loadTexts: juniSubscriberCompliance2.setDescription('The compliance statement for systems supporting subscriber operation.')
juniSubscriberLocalGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 4874, 2, 2, 49, 4, 2, 1)).setObjects(("Juniper-SUBSCRIBER-MIB", "juniSubscrLocalControl"), ("Juniper-SUBSCRIBER-MIB", "juniSubscrLocalNamePrefix"), ("Juniper-SUBSCRIBER-MIB", "juniSubscrLocalName"), ("Juniper-SUBSCRIBER-MIB", "juniSubscrLocalPasswordPrefix"), ("Juniper-SUBSCRIBER-MIB", "juniSubscrLocalPassword"), ("Juniper-SUBSCRIBER-MIB", "juniSubscrLocalDomain"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniSubscriberLocalGroup = juniSubscriberLocalGroup.setStatus('obsolete')
if mibBuilder.loadTexts: juniSubscriberLocalGroup.setDescription('Obsolete basic collection of objects providing management of locally-configured subscriber identities in a Juniper product. This group became obsolete when local authentication support was added.')
juniSubscriberLocalGroup2 = ObjectGroup((1, 3, 6, 1, 4, 1, 4874, 2, 2, 49, 4, 2, 2)).setObjects(("Juniper-SUBSCRIBER-MIB", "juniSubscrLocalControl"), ("Juniper-SUBSCRIBER-MIB", "juniSubscrLocalNamePrefix"), ("Juniper-SUBSCRIBER-MIB", "juniSubscrLocalName"), ("Juniper-SUBSCRIBER-MIB", "juniSubscrLocalPasswordPrefix"), ("Juniper-SUBSCRIBER-MIB", "juniSubscrLocalPassword"), ("Juniper-SUBSCRIBER-MIB", "juniSubscrLocalDomain"), ("Juniper-SUBSCRIBER-MIB", "juniSubscrLocalAuthentication"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniSubscriberLocalGroup2 = juniSubscriberLocalGroup2.setStatus('current')
if mibBuilder.loadTexts: juniSubscriberLocalGroup2.setDescription('The basic collection of objects providing management of locally-configured subscriber identities in a Juniper product.')
mibBuilder.exportSymbols("Juniper-SUBSCRIBER-MIB", juniSubscrLocalDomain=juniSubscrLocalDomain, juniSubscriberCompliance2=juniSubscriberCompliance2, juniSubscrLocalControl=juniSubscrLocalControl, PYSNMP_MODULE_ID=juniSubscriberMIB, juniSubscrLocalAuthentication=juniSubscrLocalAuthentication, juniSubscriberMIBCompliances=juniSubscriberMIBCompliances, JuniSubscrEncaps=JuniSubscrEncaps, juniSubscrLocalPasswordPrefix=juniSubscrLocalPasswordPrefix, juniSubscriberMIBConformance=juniSubscriberMIBConformance, juniSubscrLocal=juniSubscrLocal, juniSubscrObjects=juniSubscrObjects, juniSubscrLocalEntry=juniSubscrLocalEntry, juniSubscriberMIB=juniSubscriberMIB, juniSubscrLocalIfIndex=juniSubscrLocalIfIndex, juniSubscrLocalTable=juniSubscrLocalTable, juniSubscriberCompliance=juniSubscriberCompliance, juniSubscriberLocalGroup2=juniSubscriberLocalGroup2, juniSubscrLocalPassword=juniSubscrLocalPassword, juniSubscrLocalNamePrefix=juniSubscrLocalNamePrefix, juniSubscriberLocalGroup=juniSubscriberLocalGroup, juniSubscrLocalName=juniSubscrLocalName, juniSubscriberMIBGroups=juniSubscriberMIBGroups, juniSubscrLocalEncaps=juniSubscrLocalEncaps)
