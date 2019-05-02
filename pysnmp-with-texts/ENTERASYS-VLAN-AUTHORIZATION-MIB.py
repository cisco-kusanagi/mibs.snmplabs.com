#
# PySNMP MIB module ENTERASYS-VLAN-AUTHORIZATION-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ENTERASYS-VLAN-AUTHORIZATION-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:04:50 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint")
dot1dBasePortEntry, = mibBuilder.importSymbols("BRIDGE-MIB", "dot1dBasePortEntry")
etsysModules, = mibBuilder.importSymbols("ENTERASYS-MIB-NAMES", "etsysModules")
EnabledStatus, = mibBuilder.importSymbols("P-BRIDGE-MIB", "EnabledStatus")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
MibIdentifier, Bits, NotificationType, IpAddress, TimeTicks, Counter64, iso, Integer32, Counter32, ObjectIdentity, Unsigned32, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "Bits", "NotificationType", "IpAddress", "TimeTicks", "Counter64", "iso", "Integer32", "Counter32", "ObjectIdentity", "Unsigned32", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
etsysVlanAuthorizationMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 5624, 1, 2, 48))
etsysVlanAuthorizationMIB.setRevisions(('2004-06-02 19:22',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: etsysVlanAuthorizationMIB.setRevisionsDescriptions(('The initial version of this MIB module',))
if mibBuilder.loadTexts: etsysVlanAuthorizationMIB.setLastUpdated('200406021922Z')
if mibBuilder.loadTexts: etsysVlanAuthorizationMIB.setOrganization('Enterasys Networks, Inc')
if mibBuilder.loadTexts: etsysVlanAuthorizationMIB.setContactInfo('Postal: Enterasys Networks, Inc. 50 Minuteman Rd. Andover, MA 01810-1008 USA Phone: +1 978 684 1000 E-mail: support@enterasys.com WWW: http://www.enterasys.com')
if mibBuilder.loadTexts: etsysVlanAuthorizationMIB.setDescription("This MIB module defines a portion of the SNMP MIB under Enterasys Networks' enterprise OID pertaining to proprietary extensions to the IETF Q-BRIDGE-MIB, as specified in RFC2674, pertaining to VLAN authorization, as specified in RFC3580. Specifically, the enabling and disabling of support for the VLAN Tunnel-Type attribute returned from a RADIUS authentication, and how that attribute is applied to the port which initiated the authentication.")
class VlanAuthEgressStatus(TextualConvention, Integer32):
    description = 'The possible egress configurations which may be applied in response to a successful authentication. none(1) No egress manipulation will be made. tagged(2) The authenticating port will be added to the current egress for the VLAN-ID returned. untagged(3) The authenticating port will be added to the current untagged egress for the VLAN-ID returned. dynamic(4) The authenticating port will use information returned in the authentication response to modify the current egress lists.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("none", 1), ("tagged", 2), ("untagged", 3), ("dynamic", 4))

etsysVlanAuthorizationObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 48, 1))
etsysVlanAuthorizationSystem = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 48, 1, 1))
etsysVlanAuthorizationPorts = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 48, 1, 2))
etsysVlanAuthorizationEnable = MibScalar((1, 3, 6, 1, 4, 1, 5624, 1, 2, 48, 1, 1, 1), EnabledStatus().clone('disabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: etsysVlanAuthorizationEnable.setStatus('current')
if mibBuilder.loadTexts: etsysVlanAuthorizationEnable.setDescription('The enable/disable state for the VLAN authorization feature. When disabled, no modifications to the VLAN attributes related to packet switching should be enforced.')
etsysVlanAuthorizationTable = MibTable((1, 3, 6, 1, 4, 1, 5624, 1, 2, 48, 1, 2, 1), )
if mibBuilder.loadTexts: etsysVlanAuthorizationTable.setStatus('current')
if mibBuilder.loadTexts: etsysVlanAuthorizationTable.setDescription('Extensions to the table that contains information about every port that is associated with this transparent bridge.')
etsysVlanAuthorizationEntry = MibTableRow((1, 3, 6, 1, 4, 1, 5624, 1, 2, 48, 1, 2, 1, 1), )
dot1dBasePortEntry.registerAugmentions(("ENTERASYS-VLAN-AUTHORIZATION-MIB", "etsysVlanAuthorizationEntry"))
etsysVlanAuthorizationEntry.setIndexNames(*dot1dBasePortEntry.getIndexNames())
if mibBuilder.loadTexts: etsysVlanAuthorizationEntry.setStatus('current')
if mibBuilder.loadTexts: etsysVlanAuthorizationEntry.setDescription('A list of extensions that support the management of proprietary features for each port of a transparent bridge. This is indexed by dot1dBasePort.')
etsysVlanAuthorizationStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 48, 1, 2, 1, 1, 1), EnabledStatus().clone('enabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: etsysVlanAuthorizationStatus.setStatus('current')
if mibBuilder.loadTexts: etsysVlanAuthorizationStatus.setDescription('The enabled/disabled status for the application of VLAN authorization on this port, if disabled, the information returned in the VLAN-Tunnel-Type from the authentication will not be applied to the port (although it should be represented in this table). If enabled, those results will be applied to the port.')
etsysVlanAuthorizationAdminEgress = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 48, 1, 2, 1, 1, 2), VlanAuthEgressStatus().clone('untagged')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: etsysVlanAuthorizationAdminEgress.setStatus('current')
if mibBuilder.loadTexts: etsysVlanAuthorizationAdminEgress.setDescription('Controls the modification of the current vlan egress list (of the vlan returned in the VLAN-Tunnel-Type, and reported by etsysVlanAuthorizationVlanID) upon successful authentication in the following manner: none(1) No egress manipulation will be made. tagged(2) The authenticating port will be added to the current egress for the VLAN-ID returned. untagged(3) The authenticating port will be added to the current untagged egress for the VLAN-ID returned. dynamic(4) The authenticating port will use information returned in the authentication response to modify the current egress lists. This value is supported only if the device supports a mechanism through which the egress status may be returned through the RADIUS response. Should etsysVlanAuthorizationEnable become disabled, etsysVlanAuthorizationStatus become disabled for a port, or should etsysVlanAuthorizationVlanID become 0 or 4095, all effect on the port egress MUST be removed.')
etsysVlanAuthorizationOperEgress = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 48, 1, 2, 1, 1, 3), VlanAuthEgressStatus().clone('none')).setMaxAccess("readonly")
if mibBuilder.loadTexts: etsysVlanAuthorizationOperEgress.setStatus('current')
if mibBuilder.loadTexts: etsysVlanAuthorizationOperEgress.setDescription('Reports the current state of modification to the current vlan egress list (of the vlan returned in the VLAN-Tunnel-Type) upon successful authentication, if etsysVlanAuthorizationStatus is enabled, in the following manner: none(1) No egress manipulation will be made. tagged(2) The authenticating port will be added to the current egress for the VLAN-ID returned. untagged(3) The authenticating port will be added to the current untagged egress for the VLAN-ID returned. The purpose of this leaf is to report, specifically when etsysVlanAuthorizationAdminEgress has been set to dynamic(4), the currently enforced egress modification. If the port is unauthenticated, or no VLAN-ID has been applied, this leaf should return none(1).')
etsysVlanAuthorizationVlanID = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 48, 1, 2, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(1, 4094), ValueRangeConstraint(4095, 4095), ))).setMaxAccess("readonly")
if mibBuilder.loadTexts: etsysVlanAuthorizationVlanID.setStatus('current')
if mibBuilder.loadTexts: etsysVlanAuthorizationVlanID.setDescription('The 12 bit VLAN identifier for a given port, used to override the PVID of the given port, obtained as a result of an authentication. A value of zero indicates that there is no authenticated VLAN ID for the given port. Should a port become unauthenticated this value MUST be returned to zero. A value of 4095 indicates that a the port has been authenticated, but that the VLAN returned could not be applied to the port (possibly because of resource constraints or misconfiguration). In this instance, the original PVID should still be applied. Should the feature become disabled or the session terminate, all effect on the Port VLAN ID MUST be removed.')
etsysVlanAuthorizationConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 48, 2))
etsysVlanAuthorizationGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 48, 2, 1))
etsysVlanAuthorizationCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 48, 2, 2))
etsysVlanAuthorizationGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 5624, 1, 2, 48, 2, 1, 1)).setObjects(("ENTERASYS-VLAN-AUTHORIZATION-MIB", "etsysVlanAuthorizationEnable"), ("ENTERASYS-VLAN-AUTHORIZATION-MIB", "etsysVlanAuthorizationStatus"), ("ENTERASYS-VLAN-AUTHORIZATION-MIB", "etsysVlanAuthorizationAdminEgress"), ("ENTERASYS-VLAN-AUTHORIZATION-MIB", "etsysVlanAuthorizationOperEgress"), ("ENTERASYS-VLAN-AUTHORIZATION-MIB", "etsysVlanAuthorizationVlanID"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    etsysVlanAuthorizationGroup = etsysVlanAuthorizationGroup.setStatus('current')
if mibBuilder.loadTexts: etsysVlanAuthorizationGroup.setDescription('A collection of objects relating to VLAN Authorization.')
etsysVlanAuthorizationCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 5624, 1, 2, 48, 2, 2, 1)).setObjects(("ENTERASYS-VLAN-AUTHORIZATION-MIB", "etsysVlanAuthorizationGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    etsysVlanAuthorizationCompliance = etsysVlanAuthorizationCompliance.setStatus('current')
if mibBuilder.loadTexts: etsysVlanAuthorizationCompliance.setDescription('The compliance statement for devices that support the Enterasys VLAN Authorization MIB.')
mibBuilder.exportSymbols("ENTERASYS-VLAN-AUTHORIZATION-MIB", etsysVlanAuthorizationVlanID=etsysVlanAuthorizationVlanID, etsysVlanAuthorizationGroup=etsysVlanAuthorizationGroup, etsysVlanAuthorizationEnable=etsysVlanAuthorizationEnable, etsysVlanAuthorizationOperEgress=etsysVlanAuthorizationOperEgress, etsysVlanAuthorizationAdminEgress=etsysVlanAuthorizationAdminEgress, etsysVlanAuthorizationConformance=etsysVlanAuthorizationConformance, VlanAuthEgressStatus=VlanAuthEgressStatus, etsysVlanAuthorizationPorts=etsysVlanAuthorizationPorts, etsysVlanAuthorizationStatus=etsysVlanAuthorizationStatus, etsysVlanAuthorizationCompliance=etsysVlanAuthorizationCompliance, etsysVlanAuthorizationMIB=etsysVlanAuthorizationMIB, etsysVlanAuthorizationGroups=etsysVlanAuthorizationGroups, etsysVlanAuthorizationObjects=etsysVlanAuthorizationObjects, etsysVlanAuthorizationTable=etsysVlanAuthorizationTable, etsysVlanAuthorizationSystem=etsysVlanAuthorizationSystem, etsysVlanAuthorizationEntry=etsysVlanAuthorizationEntry, etsysVlanAuthorizationCompliances=etsysVlanAuthorizationCompliances, PYSNMP_MODULE_ID=etsysVlanAuthorizationMIB)
