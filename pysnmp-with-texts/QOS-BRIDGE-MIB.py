#
# PySNMP MIB module QOS-BRIDGE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/QOS-BRIDGE-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:43:59 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection")
dot1qVlanIndex, = mibBuilder.importSymbols("Q-BRIDGE-MIB", "dot1qVlanIndex")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
Gauge32, Bits, TimeTicks, iso, MibIdentifier, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, IpAddress, NotificationType, mib_2, Integer32, Counter64, Counter32, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "Bits", "TimeTicks", "iso", "MibIdentifier", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "IpAddress", "NotificationType", "mib-2", "Integer32", "Counter64", "Counter32", "ModuleIdentity")
DisplayString, RowStatus, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "RowStatus", "TextualConvention")
dot1dQosMib = ModuleIdentity((1, 3, 6, 1, 2, 1, 12346))
dot1dQosMib.setRevisions(('2000-06-07 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: dot1dQosMib.setRevisionsDescriptions(('Initial version, published as RFC xxxx.',))
if mibBuilder.loadTexts: dot1dQosMib.setLastUpdated('200006070000Z')
if mibBuilder.loadTexts: dot1dQosMib.setOrganization('Extreme Networks')
if mibBuilder.loadTexts: dot1dQosMib.setContactInfo(' Andrew Smith (author) Extreme Networks 3585 Monroe St. Santa Clara, CA 95051, USA E-mail: andrew@extremenetworks.com')
if mibBuilder.loadTexts: dot1dQosMib.setDescription("This MIB defines the additional objects necessary to manage the Quality-of-Service aspects of a bridge device that uses the IETF's Differentiated Services Architecture described in RFC 2475 and the Conceptual Model for DiffServ Routers in draft-ietf- diffserv-model-03.txt. It is to be used in conjunction with the Diffserv MIB described in draft-ietf-diffserv-mib-03.txt.")
dot1dQosObjects = MibIdentifier((1, 3, 6, 1, 2, 1, 12346, 1))
dot1dQosTables = MibIdentifier((1, 3, 6, 1, 2, 1, 12346, 2))
dot1dQosMIBConformance = MibIdentifier((1, 3, 6, 1, 2, 1, 12346, 3))
class Dot1dUserPri(TextualConvention, Integer32):
    description = 'The IEEE 802.1 user_priority that may be used for discriminating or marking a traffic stream.'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 7)

dot1dQosUserPriTable = MibTable((1, 3, 6, 1, 2, 1, 12346, 2, 1), )
if mibBuilder.loadTexts: dot1dQosUserPriTable.setReference('[MODEL] section 4.2.4')
if mibBuilder.loadTexts: dot1dQosUserPriTable.setStatus('current')
if mibBuilder.loadTexts: dot1dQosUserPriTable.setDescription('A table of user_priority entries that each signifies a traffic class in 802.1D bridges. All entries exist in this table at all times. Its entries may be used as destinations for diffServClassifierFilter pointers for traffic classification purposes and for diffServActionSpecific pointers for traffic marking purposes.')
dot1dQosUserPriEntry = MibTableRow((1, 3, 6, 1, 2, 1, 12346, 2, 1, 1), ).setIndexNames((0, "QOS-BRIDGE-MIB", "dot1dQosUserPri"))
if mibBuilder.loadTexts: dot1dQosUserPriEntry.setStatus('current')
if mibBuilder.loadTexts: dot1dQosUserPriEntry.setDescription('An entry that describes a single 802.1D user_priority filter.')
dot1dQosUserPri = MibTableColumn((1, 3, 6, 1, 2, 1, 12346, 2, 1, 1, 1), Dot1dUserPri()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1dQosUserPri.setStatus('current')
if mibBuilder.loadTexts: dot1dQosUserPri.setDescription('A user_priority value for the filter. Filters may be shared by multiple interfaces in the same system.')
dot1dQosVlanClfrTable = MibTable((1, 3, 6, 1, 2, 1, 12346, 2, 2), )
if mibBuilder.loadTexts: dot1dQosVlanClfrTable.setReference('[MODEL] section 4.2.4, [BRIDGEMIB] dot1qVlanCurrentTable.')
if mibBuilder.loadTexts: dot1dQosVlanClfrTable.setStatus('current')
if mibBuilder.loadTexts: dot1dQosVlanClfrTable.setDescription('A table of VLAN entries for use in QoS classification in bridges. Its entries may be used as destinations for diffServClassifierFilter pointers for traffic classification purposes.')
dot1dQosVlanClfrEntry = MibTableRow((1, 3, 6, 1, 2, 1, 12346, 2, 2, 1), ).setIndexNames((0, "Q-BRIDGE-MIB", "dot1qVlanIndex"))
if mibBuilder.loadTexts: dot1dQosVlanClfrEntry.setStatus('current')
if mibBuilder.loadTexts: dot1dQosVlanClfrEntry.setDescription('An entry that describes a classifier element for a single 802.1Q VLAN.')
dot1dQosVlanStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 12346, 2, 2, 1, 1), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dot1dQosVlanStatus.setStatus('current')
if mibBuilder.loadTexts: dot1dQosVlanStatus.setDescription('The RowStatus variable controls the activation, deactivation, or deletion of a filter for a VLAN for use in QoS classification. Note that, even though this table is indexed by dot1qVlanIndex, this does not imply that there must be an equivalent entry in either dot1qVlanCurrentTable or dot1qVlanStaticTable.')
dot1dQosMIBCompliances = MibIdentifier((1, 3, 6, 1, 2, 1, 12346, 3, 1))
dot1dQosMIBGroups = MibIdentifier((1, 3, 6, 1, 2, 1, 12346, 3, 2))
dot1dQosMIBCompliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 12346, 3, 1, 1)).setObjects(("QOS-BRIDGE-MIB", "dot1dQosMIBUserPriGroup"), ("QOS-BRIDGE-MIB", "dot1dQosMIBVlanGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    dot1dQosMIBCompliance = dot1dQosMIBCompliance.setStatus('current')
if mibBuilder.loadTexts: dot1dQosMIBCompliance.setDescription('This MIB may be implemented as a read-only or as a read-create MIB.')
dot1dQosMIBUserPriGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 12346, 3, 2, 1)).setObjects(("QOS-BRIDGE-MIB", "dot1dQosUserPri"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    dot1dQosMIBUserPriGroup = dot1dQosMIBUserPriGroup.setStatus('current')
if mibBuilder.loadTexts: dot1dQosMIBUserPriGroup.setDescription('The user_priority Group defines the MIB Objects that represent 802.1D user_priority values and describe a table of entries that may be used as destinations for diffServClassifierFilter and diffServActionSpecific pointers.')
dot1dQosMIBVlanGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 12346, 3, 2, 2)).setObjects(("QOS-BRIDGE-MIB", "dot1dQosVlanStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    dot1dQosMIBVlanGroup = dot1dQosMIBVlanGroup.setStatus('current')
if mibBuilder.loadTexts: dot1dQosMIBVlanGroup.setDescription('The VLAN Group defines the MIB Objects that represent VLANs and describe a table of entries that may be used as destinations for diffServClassifierFilter pointers.')
mibBuilder.exportSymbols("QOS-BRIDGE-MIB", dot1dQosUserPriTable=dot1dQosUserPriTable, dot1dQosVlanClfrEntry=dot1dQosVlanClfrEntry, dot1dQosMIBUserPriGroup=dot1dQosMIBUserPriGroup, dot1dQosMIBGroups=dot1dQosMIBGroups, dot1dQosUserPri=dot1dQosUserPri, dot1dQosMIBCompliances=dot1dQosMIBCompliances, dot1dQosMib=dot1dQosMib, dot1dQosMIBConformance=dot1dQosMIBConformance, dot1dQosTables=dot1dQosTables, dot1dQosVlanStatus=dot1dQosVlanStatus, Dot1dUserPri=Dot1dUserPri, dot1dQosMIBVlanGroup=dot1dQosMIBVlanGroup, PYSNMP_MODULE_ID=dot1dQosMib, dot1dQosObjects=dot1dQosObjects, dot1dQosVlanClfrTable=dot1dQosVlanClfrTable, dot1dQosMIBCompliance=dot1dQosMIBCompliance, dot1dQosUserPriEntry=dot1dQosUserPriEntry)
