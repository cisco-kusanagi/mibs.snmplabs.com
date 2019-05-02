#
# PySNMP MIB module ENTERASYS-IF-MIB-EXT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ENTERASYS-IF-MIB-EXT-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:03:40 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion")
etsysModules, = mibBuilder.importSymbols("ENTERASYS-MIB-NAMES", "etsysModules")
ifEntry, = mibBuilder.importSymbols("IF-MIB", "ifEntry")
EnabledStatus, = mibBuilder.importSymbols("P-BRIDGE-MIB", "EnabledStatus")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
NotificationType, ModuleIdentity, Counter32, TimeTicks, MibIdentifier, Counter64, ObjectIdentity, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, Unsigned32, Gauge32, Bits, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "ModuleIdentity", "Counter32", "TimeTicks", "MibIdentifier", "Counter64", "ObjectIdentity", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "Unsigned32", "Gauge32", "Bits", "IpAddress")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
etsysIfMibExtMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 5624, 1, 2, 57))
etsysIfMibExtMIB.setRevisions(('2011-05-12 14:15', '2005-01-13 21:35',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: etsysIfMibExtMIB.setRevisionsDescriptions(('Addition of Ethernet OAM and Ethernet OAM Loopback causes to the EtsysIfOperStatusCauses textual convention.', 'The initial version of this MIB module.',))
if mibBuilder.loadTexts: etsysIfMibExtMIB.setLastUpdated('201105121415Z')
if mibBuilder.loadTexts: etsysIfMibExtMIB.setOrganization('Enterasys Networks, Inc.')
if mibBuilder.loadTexts: etsysIfMibExtMIB.setContactInfo('Postal: Enterasys Networks 50 Minuteman Rd. Andover, MA 01810-1008 USA Phone: +1 978 684 1000 E-mail: support@enterasys.com WWW: http://www.enterasys.com')
if mibBuilder.loadTexts: etsysIfMibExtMIB.setDescription('This MIB module defines a portion of the SNMP MIB under the Enterasys Networks enterprise OID that provide extensions to the industry standard IF-MIB.')
class EtsysIfOperStatusCauses(TextualConvention, Bits):
    reference = "RFC 2863, 'The Interfaces Group MIB' ENTERASYS-LINK-FLAP-MIB ENTERASYS-FLOW-LIMITING-MIB ENTERASYS-POLICY-PROFILE-MIB ENTERASYS-CLASS-OF-SERVICE-MIB ENTERASYS-ETH-OAM-EXT-MIB IEEE Std. 802.1X-2001 IEEE Std. 802.3-2002"
    description = "This convention specifies the variety of functionalities that may cause an interface's ifOperStatus to be have a value other than up(1). A set bit indicates that the associated cause is influencing the interface's current ifOperStatus. adminStatus(0) - The ifAdminStatus for the interface is not up(1). linkLoss(1) - The interface has physically lost link with its partner. linkFlap(2) - The interface has been brought down by the Link Flap feature as defined by etsysLinkFlapMIB. self(3) - The interface has brought itself down. initialization(4) - The system or interface is still in the process of initializing itself. flowLimiting(5) - The interface has been brought down by the Flow Limiting feature as defined by etsysFlowLimitingMIB. policy(6) - The interface has been brought down by the Policy feature as defined by etsysPolicyProfileMIB. classOfService(7) - The interface has been brought down by the rate limiting feature defined by etsysCosMIB. ieee8021x(8) - The interface has been made dormant awaiting successful authentication by 802.1X. ieee8023lag(9) - The interface has been made dormant as a result of being an underlying physical port in a Link Aggregation. enetOam(10) - The interface has been brought down by the Ethernet OAM feature as defined by etsysEthOamExtMIB. enetOamLb(11) - The interface has been brought down by the Ethernet OAM loopback feature as defined by dot3OamMIB."
    status = 'current'
    namedValues = NamedValues(("adminStatus", 0), ("linkLoss", 1), ("linkFlap", 2), ("self", 3), ("initialization", 4), ("flowLimiting", 5), ("policy", 6), ("classOfService", 7), ("ieee8021x", 8), ("ieee8023lag", 9), ("enetOam", 10), ("enetOamLb", 11))

etsysIfMibExtObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 57, 1))
etsysIfMibExtSystem = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 57, 1, 1))
etsysIfMibExtInterface = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 57, 1, 2))
etsysIfOperStateLinkChange = MibScalar((1, 3, 6, 1, 4, 1, 5624, 1, 2, 57, 1, 1, 1), EnabledStatus().clone('disabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: etsysIfOperStateLinkChange.setStatus('current')
if mibBuilder.loadTexts: etsysIfOperStateLinkChange.setDescription("This object controls the system wide ability to manipulate the physical link state of an interface when the interface's ifOperStatus transitions into or out of the down(2) state. A value of enabled(1) will cause an interface to drop physical link when its ifOperStatus transitions to down(2). If the interface would transition out of the down(2) state, assuming it did have link, then physical link will be restored to the interface. A value of disabled(2) will cause an interface to not alter its physical link regardless of the value of ifOperStatus. This object only affects those interfaces which have a concept of physical link.")
etsysInterfaceExtTable = MibTable((1, 3, 6, 1, 4, 1, 5624, 1, 2, 57, 1, 2, 1), )
if mibBuilder.loadTexts: etsysInterfaceExtTable.setStatus('current')
if mibBuilder.loadTexts: etsysInterfaceExtTable.setDescription('A table of per interface information that extends the base ifTable defined in RFC2863.')
etsysInterfaceExtEntry = MibTableRow((1, 3, 6, 1, 4, 1, 5624, 1, 2, 57, 1, 2, 1, 1), )
ifEntry.registerAugmentions(("ENTERASYS-IF-MIB-EXT-MIB", "etsysInterfaceExtEntry"))
etsysInterfaceExtEntry.setIndexNames(*ifEntry.getIndexNames())
if mibBuilder.loadTexts: etsysInterfaceExtEntry.setStatus('current')
if mibBuilder.loadTexts: etsysInterfaceExtEntry.setDescription('An entry containing per interface information.')
etsysIfOperStatusCause = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 57, 1, 2, 1, 1, 1), EtsysIfOperStatusCauses()).setMaxAccess("readonly")
if mibBuilder.loadTexts: etsysIfOperStatusCause.setStatus('current')
if mibBuilder.loadTexts: etsysIfOperStatusCause.setDescription('This object indicates the various features that could cause the ifOperStatus of an interface to not be up(1).')
etsysIfMibExtConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 57, 2))
etsysIfMibExtGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 57, 2, 1))
etsysIfMibExtCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 57, 2, 2))
etsysIfMibExtOperLinkGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 5624, 1, 2, 57, 2, 1, 1)).setObjects(("ENTERASYS-IF-MIB-EXT-MIB", "etsysIfOperStateLinkChange"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    etsysIfMibExtOperLinkGroup = etsysIfMibExtOperLinkGroup.setStatus('current')
if mibBuilder.loadTexts: etsysIfMibExtOperLinkGroup.setDescription('The group that controls physical link manipulation as a result of ifOperStatus changes.')
etsysIfMibExtOperStatusGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 5624, 1, 2, 57, 2, 1, 2)).setObjects(("ENTERASYS-IF-MIB-EXT-MIB", "etsysIfOperStatusCause"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    etsysIfMibExtOperStatusGroup = etsysIfMibExtOperStatusGroup.setStatus('current')
if mibBuilder.loadTexts: etsysIfMibExtOperStatusGroup.setDescription('The group that provides the cause of the current ifOperStatus value for a given interface.')
etsysIfMibExtCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 5624, 1, 2, 57, 2, 2, 1)).setObjects(("ENTERASYS-IF-MIB-EXT-MIB", "etsysIfMibExtOperLinkGroup"), ("ENTERASYS-IF-MIB-EXT-MIB", "etsysIfMibExtOperStatusGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    etsysIfMibExtCompliance = etsysIfMibExtCompliance.setStatus('current')
if mibBuilder.loadTexts: etsysIfMibExtCompliance.setDescription('The compliance statement for devices that support IF-MIB extensions.')
mibBuilder.exportSymbols("ENTERASYS-IF-MIB-EXT-MIB", etsysIfMibExtObjects=etsysIfMibExtObjects, etsysIfMibExtOperLinkGroup=etsysIfMibExtOperLinkGroup, EtsysIfOperStatusCauses=EtsysIfOperStatusCauses, etsysIfMibExtOperStatusGroup=etsysIfMibExtOperStatusGroup, etsysIfMibExtCompliance=etsysIfMibExtCompliance, etsysIfMibExtCompliances=etsysIfMibExtCompliances, etsysIfOperStatusCause=etsysIfOperStatusCause, etsysInterfaceExtEntry=etsysInterfaceExtEntry, etsysIfMibExtConformance=etsysIfMibExtConformance, PYSNMP_MODULE_ID=etsysIfMibExtMIB, etsysIfMibExtMIB=etsysIfMibExtMIB, etsysIfOperStateLinkChange=etsysIfOperStateLinkChange, etsysIfMibExtSystem=etsysIfMibExtSystem, etsysIfMibExtInterface=etsysIfMibExtInterface, etsysInterfaceExtTable=etsysInterfaceExtTable, etsysIfMibExtGroups=etsysIfMibExtGroups)
