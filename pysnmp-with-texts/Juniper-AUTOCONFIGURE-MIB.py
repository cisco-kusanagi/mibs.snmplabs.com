#
# PySNMP MIB module Juniper-AUTOCONFIGURE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Juniper-AUTOCONFIGURE-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:01:49 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
juniMibs, = mibBuilder.importSymbols("Juniper-MIBs", "juniMibs")
JuniEnable, = mibBuilder.importSymbols("Juniper-TC", "JuniEnable")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, Gauge32, MibIdentifier, ModuleIdentity, NotificationType, IpAddress, Counter64, Bits, TimeTicks, Unsigned32, Integer32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "Gauge32", "MibIdentifier", "ModuleIdentity", "NotificationType", "IpAddress", "Counter64", "Bits", "TimeTicks", "Unsigned32", "Integer32", "iso")
DisplayString, TruthValue, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TruthValue", "TextualConvention")
juniAutoConfMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 4874, 2, 2, 48))
juniAutoConfMIB.setRevisions(('2004-07-26 19:54', '2002-11-22 16:08', '2002-11-22 15:24', '2000-11-16 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: juniAutoConfMIB.setRevisionsDescriptions(('Added Encapsulation Type Lockout objects.', 'Replaced Unisphere names with Juniper names.', 'Added bridgedEthernet(19) to JuniAutoConfEncaps.', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: juniAutoConfMIB.setLastUpdated('200407261954Z')
if mibBuilder.loadTexts: juniAutoConfMIB.setOrganization('Juniper Networks')
if mibBuilder.loadTexts: juniAutoConfMIB.setContactInfo(' Juniper Networks, Inc. Postal: 10 Technology Park Drive Westford MA 01886-3146 USA Tel: +1 978 589 5800 Email: mib@Juniper.net')
if mibBuilder.loadTexts: juniAutoConfMIB.setDescription('The Auto-Configuration MIB for the Juniper Networks enterprise.')
class JuniAutoConfEncaps(TextualConvention, Integer32):
    description = 'Encapsulated protocol type.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 17, 19))
    namedValues = NamedValues(("ip", 0), ("ppp", 1), ("pppoe", 17), ("bridgedEthernet", 19))

juniAutoConfObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 48, 1))
juniAutoConf = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 48, 1, 1))
juniAutoConfTable = MibTable((1, 3, 6, 1, 4, 1, 4874, 2, 2, 48, 1, 1, 1), )
if mibBuilder.loadTexts: juniAutoConfTable.setStatus('current')
if mibBuilder.loadTexts: juniAutoConfTable.setDescription('Configures recognition of incoming data encapsulation types that trigger autoconfiguration on an interface. Also, configures the time range that the encapsulation type will be locked-out from recognition in the event of an error in creating an interface of the encapsulation type.')
juniAutoConfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4874, 2, 2, 48, 1, 1, 1, 1), ).setIndexNames((0, "Juniper-AUTOCONFIGURE-MIB", "juniAutoConfIfIndex"), (0, "Juniper-AUTOCONFIGURE-MIB", "juniAutoConfEncaps"))
if mibBuilder.loadTexts: juniAutoConfEntry.setStatus('current')
if mibBuilder.loadTexts: juniAutoConfEntry.setDescription('Configures recognition of an incoming data encapsulation type that triggers autoconfiguration on an interface. Also, configures the time range that the encapsulation type will be locked-out from recognition in the event of an error in creating an interface of the encapsulation type.')
juniAutoConfIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 48, 1, 1, 1, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: juniAutoConfIfIndex.setStatus('current')
if mibBuilder.loadTexts: juniAutoConfIfIndex.setDescription('The ifIndex of the interface to which the autoconfiguration information in this entry applies.')
juniAutoConfEncaps = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 48, 1, 1, 1, 1, 2), JuniAutoConfEncaps())
if mibBuilder.loadTexts: juniAutoConfEncaps.setStatus('current')
if mibBuilder.loadTexts: juniAutoConfEncaps.setDescription('The encapsulated protocol type to which the autoconfiguration information in this entry applies.')
juniAutoConfEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 48, 1, 1, 1, 1, 3), JuniEnable()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: juniAutoConfEnable.setStatus('current')
if mibBuilder.loadTexts: juniAutoConfEnable.setDescription('When enabled, permits autoconfiguration of the specified interface when the specified encapsulation is recognized in an incoming data frame.')
juniAutoConfLockoutSupported = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 48, 1, 1, 1, 1, 4), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: juniAutoConfLockoutSupported.setStatus('current')
if mibBuilder.loadTexts: juniAutoConfLockoutSupported.setDescription('Indicates whether lockout is supported for the specified encapsulation type for the specified interface. If lockout is supported, then juniAutoConfLockoutMin, juniAutoConfLockoutMax, juniAutoConfLockoutTime, juniAutoConfLockoutElapsedTime, and juniAutoConfNextLockoutTime are valid and supported in this entry.')
juniAutoConfLockoutMin = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 48, 1, 1, 1, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 86400)).clone(1)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: juniAutoConfLockoutMin.setStatus('current')
if mibBuilder.loadTexts: juniAutoConfLockoutMin.setDescription("The lower bound, in seconds, of the time range used to specify the duration of the lockout of the encapsulation type from recognition for the specified interface. This only takes effect if juniAutoConfEnable is set to enable for the encapsulation type for this interface. The ability to lockout the specified encapsulation type from recognition in the event of an error in creating an interface of the encapsulation type is enabled by default. The initial lockout duration is this object's value and increases exponentially for each failure that occurs for the specified encapsulation type for the specified interface within the greater of 15 minutes and juniAutoConfLockoutMax. The lockout duration for the specified encapsulation type will not exceed juniAutoConfLockoutMax. If the time between creation errors for the specified encapsulation type for the specified interface is greater than the greater of 15 minutes and juniAutoConfigLockoutMax, then the lockout duration reverts to this object's value. To disable the ability to lockout the specified encapsulation type from recognition in the event of an error in creating an interface of the encapsulation type for the specified interface, the value of this object and juniAutoConfLockoutMax must be set to 0. It is not recommended that this lockout feature be disabled except for debugging purposes.")
juniAutoConfLockoutMax = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 48, 1, 1, 1, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 86400)).clone(300)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: juniAutoConfLockoutMax.setStatus('current')
if mibBuilder.loadTexts: juniAutoConfLockoutMax.setDescription("The upper bound, in seconds, of the time range used to specify the duration of the lockout of the encapsulation type from recognition for the specified interface. This value must equal or exceed the value for juniAutoConfLockoutMin. This only takes effect if juniAutoConfEnable is set to enable for the encapsulation type for this interface. The ability to lockout the specified encapsulation type from recognition in the event of an error in creating an interface of the encapsulation type is enabled by default. The initial lockout duration is juniAutoConfLockoutMin and increases exponentially for each failure that occurs for the specified encapsulation type for the specified interface within the greater of 15 minutes and this object's value. The lockout duration for the specified encapsulation type will not exceed this object's value. If the time between creation errors for the specified encapsulation type for the specified interface is greater than the greater of 15 minutes and this object's value, then the lockout duration reverts to juniAutoConfigLockoutMin. To disable the ability to lockout the specified encapsulation type from recognition in the event of an error in creating an interface of the encapsulation type for the specified interface, the value of this object and juniAutoConfLockoutMin must be set to 0. It is not recommended that this lockout feature be disabled except for debugging purposes.")
juniAutoConfLockoutTime = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 48, 1, 1, 1, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 86400))).setMaxAccess("readonly")
if mibBuilder.loadTexts: juniAutoConfLockoutTime.setStatus('current')
if mibBuilder.loadTexts: juniAutoConfLockoutTime.setDescription('The time duration, in seconds, currently used to lockout the specified encapsulation type from recognition for the specified interface. The reported value is within the range specified by juniAutoConfLockoutMin and juniAutoConfLockoutMax. A value of 0 indicates that no lockout is occurring for the encapsulation type for the specified interface.')
juniAutoConfLockoutElapsedTime = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 48, 1, 1, 1, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 86400))).setMaxAccess("readonly")
if mibBuilder.loadTexts: juniAutoConfLockoutElapsedTime.setStatus('current')
if mibBuilder.loadTexts: juniAutoConfLockoutElapsedTime.setDescription('The elapsed time, in seconds, that the specified encapsulation type has been locked-out from recognition for the specified interface. Its value will not exceed that of juniAutoConfLockoutTime. A value of 0 indicates that no lockout is occurring for the encapsulation type for the specified interface.')
juniAutoConfNextLockoutTime = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 48, 1, 1, 1, 1, 9), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 86400))).setMaxAccess("readonly")
if mibBuilder.loadTexts: juniAutoConfNextLockoutTime.setStatus('current')
if mibBuilder.loadTexts: juniAutoConfNextLockoutTime.setDescription('The time duration, in seconds, that will be used to lockout the specified encapsulation type from recognition for the specified interface for the next event that results in a lockout condition. The reported value is within the range specified by juniAutoConfLockoutMin and juniAutoConfLockoutMax. When juniAutoConfEnable is set to enable, a value of 0 indicates that lockout is prevented from occurring for the encapsulation type for the specified interface (i.e., juniAutoConfLockoutMin and juniAutoConfLockoutMax are both set to 0).')
juniAutoConfMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 48, 4))
juniAutoConfMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 48, 4, 1))
juniAutoConfMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 48, 4, 2))
juniAutoConfCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 4874, 2, 2, 48, 4, 1, 1)).setObjects(("Juniper-AUTOCONFIGURE-MIB", "juniAutoConfGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniAutoConfCompliance = juniAutoConfCompliance.setStatus('obsolete')
if mibBuilder.loadTexts: juniAutoConfCompliance.setDescription('Obsolete compliance statement for systems supporting enabling of autoconfiguration operation. This statement was obsoleted when encapsulation type lockout objects were added.')
juniAutoConfCompliance2 = ModuleCompliance((1, 3, 6, 1, 4, 1, 4874, 2, 2, 48, 4, 1, 2)).setObjects(("Juniper-AUTOCONFIGURE-MIB", "juniAutoConfGroup2"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniAutoConfCompliance2 = juniAutoConfCompliance2.setStatus('current')
if mibBuilder.loadTexts: juniAutoConfCompliance2.setDescription('The compliance statement for systems supporting enabling of autoconfiguration operation.')
juniAutoConfGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 4874, 2, 2, 48, 4, 2, 1)).setObjects(("Juniper-AUTOCONFIGURE-MIB", "juniAutoConfEnable"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniAutoConfGroup = juniAutoConfGroup.setStatus('obsolete')
if mibBuilder.loadTexts: juniAutoConfGroup.setDescription('Obsoleted collection of objects providing management of autoconfiguration enabling in a Juniper product. This group became obsolete when Encapsulation Type Lockout support was added.')
juniAutoConfGroup2 = ObjectGroup((1, 3, 6, 1, 4, 1, 4874, 2, 2, 48, 4, 2, 2)).setObjects(("Juniper-AUTOCONFIGURE-MIB", "juniAutoConfLockoutSupported"), ("Juniper-AUTOCONFIGURE-MIB", "juniAutoConfLockoutMin"), ("Juniper-AUTOCONFIGURE-MIB", "juniAutoConfLockoutMax"), ("Juniper-AUTOCONFIGURE-MIB", "juniAutoConfLockoutTime"), ("Juniper-AUTOCONFIGURE-MIB", "juniAutoConfLockoutElapsedTime"), ("Juniper-AUTOCONFIGURE-MIB", "juniAutoConfNextLockoutTime"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniAutoConfGroup2 = juniAutoConfGroup2.setStatus('current')
if mibBuilder.loadTexts: juniAutoConfGroup2.setDescription('The basic collection of objects providing management of autoconfiguration enabling in a Juniper product.')
mibBuilder.exportSymbols("Juniper-AUTOCONFIGURE-MIB", juniAutoConf=juniAutoConf, juniAutoConfGroup=juniAutoConfGroup, juniAutoConfObjects=juniAutoConfObjects, juniAutoConfEntry=juniAutoConfEntry, juniAutoConfMIBCompliances=juniAutoConfMIBCompliances, juniAutoConfLockoutMax=juniAutoConfLockoutMax, juniAutoConfCompliance=juniAutoConfCompliance, juniAutoConfTable=juniAutoConfTable, juniAutoConfLockoutElapsedTime=juniAutoConfLockoutElapsedTime, juniAutoConfLockoutTime=juniAutoConfLockoutTime, juniAutoConfEnable=juniAutoConfEnable, juniAutoConfMIBGroups=juniAutoConfMIBGroups, JuniAutoConfEncaps=JuniAutoConfEncaps, juniAutoConfNextLockoutTime=juniAutoConfNextLockoutTime, juniAutoConfLockoutMin=juniAutoConfLockoutMin, juniAutoConfMIB=juniAutoConfMIB, juniAutoConfEncaps=juniAutoConfEncaps, juniAutoConfGroup2=juniAutoConfGroup2, PYSNMP_MODULE_ID=juniAutoConfMIB, juniAutoConfIfIndex=juniAutoConfIfIndex, juniAutoConfLockoutSupported=juniAutoConfLockoutSupported, juniAutoConfMIBConformance=juniAutoConfMIBConformance, juniAutoConfCompliance2=juniAutoConfCompliance2)
