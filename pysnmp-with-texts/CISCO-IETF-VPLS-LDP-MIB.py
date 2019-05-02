#
# PySNMP MIB module CISCO-IETF-VPLS-LDP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-IETF-VPLS-LDP-MIB
# Produced by pysmi-0.3.4 at Wed May  1 12:01:11 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint")
cvplsPwBindIndex, cvplsConfigIndex = mibBuilder.importSymbols("CISCO-IETF-VPLS-GENERIC-MIB", "cvplsPwBindIndex", "cvplsConfigIndex")
ciscoExperiment, = mibBuilder.importSymbols("CISCO-SMI", "ciscoExperiment")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, ModuleIdentity, iso, TimeTicks, NotificationType, Counter64, Integer32, Gauge32, Unsigned32, IpAddress, Bits, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "ModuleIdentity", "iso", "TimeTicks", "NotificationType", "Counter64", "Integer32", "Gauge32", "Unsigned32", "IpAddress", "Bits", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32")
TextualConvention, DisplayString, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString", "TruthValue")
VPNId, = mibBuilder.importSymbols("VPN-TC-STD-MIB", "VPNId")
cvplsLdpMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 10, 141))
cvplsLdpMIB.setRevisions(('2007-11-22 12:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: cvplsLdpMIB.setRevisionsDescriptions(('Initial version of this MIB.',))
if mibBuilder.loadTexts: cvplsLdpMIB.setLastUpdated('200711221200Z')
if mibBuilder.loadTexts: cvplsLdpMIB.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: cvplsLdpMIB.setContactInfo('Cisco Systems Customer Service Postal: 170 W Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-l2vpn@cisco.com')
if mibBuilder.loadTexts: cvplsLdpMIB.setDescription('This MIB module contains managed object definitions for LDP signalled Virtual Private LAN Services as in [L2VPN-VPLS-LDP] This MIB module enables the use of any underlying Pseudo Wire network. This MIB is based on the following IETF document. http://www1.tools.ietf.org/html/draft-nadeau-l2vpn-vpls-mib-03')
cvplsLdpObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 141, 1))
cvplsLdpConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 141, 2))
cvplsLdpConfigTable = MibTable((1, 3, 6, 1, 4, 1, 9, 10, 141, 1, 1), )
if mibBuilder.loadTexts: cvplsLdpConfigTable.setStatus('current')
if mibBuilder.loadTexts: cvplsLdpConfigTable.setDescription('This table specifies information for configuring and monitoring LDP specific parameters for Virtual Private Lan Services(VPLS).')
cvplsLdpConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 10, 141, 1, 1, 1), ).setIndexNames((0, "CISCO-IETF-VPLS-GENERIC-MIB", "cvplsConfigIndex"))
if mibBuilder.loadTexts: cvplsLdpConfigEntry.setStatus('current')
if mibBuilder.loadTexts: cvplsLdpConfigEntry.setDescription('A row in this table represents LDP specific information for Virtual Private Lan Service(VPLS) in a packet network. It is indexed by cvplsConfigIndex, which uniquely identifies a single VPLS. A row is automatically created when a VPLS service is configured using LDP signalling. None of the read-create objects values can be changed when cvplsRowStatus is in the active(1) state. Changes are allowed when the cvplsRowStatus is in notInService(2) or notReady(3) states only. If the operator need to change one of the values for an active row the cvplsConfigRowStatus should be first changed to notInService(2), the objects may be changed now, and later to active(1) in order to re-initiate the signaling process with the new values in effect.')
cvplsLdpConfigMacAddrWithdraw = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 141, 1, 1, 1, 1), TruthValue().clone('true')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cvplsLdpConfigMacAddrWithdraw.setStatus('current')
if mibBuilder.loadTexts: cvplsLdpConfigMacAddrWithdraw.setDescription('This object specifies if MAC address withdrawl is enabled in this service. If this object is true then Mac address withdrawl Learning is enabled. If false, then Mac Learning is disabled.')
cvplsLdpPwBindTable = MibTable((1, 3, 6, 1, 4, 1, 9, 10, 141, 1, 2), )
if mibBuilder.loadTexts: cvplsLdpPwBindTable.setStatus('current')
if mibBuilder.loadTexts: cvplsLdpPwBindTable.setDescription('This table provides LDP specific information for an association between a VPLS service and the corresponding Pseudo Wires. A service can have more than one Pseudo Wire association. Pseudo Wires are defined in the cpwTable.')
cvplsLdpPwBindEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 10, 141, 1, 2, 1), ).setIndexNames((0, "CISCO-IETF-VPLS-GENERIC-MIB", "cvplsConfigIndex"), (0, "CISCO-IETF-VPLS-GENERIC-MIB", "cvplsPwBindIndex"))
if mibBuilder.loadTexts: cvplsLdpPwBindEntry.setStatus('current')
if mibBuilder.loadTexts: cvplsLdpPwBindEntry.setDescription('Each row represents an association between a VPLS instance and one or more Pseudo Wires defined in the cpwTable. Each index is unique in describing an entry in this table. However both indexes are required to define the one to many association of service to pseudowire. An entry in this table is instantiated only when LDP signalling is used to configure VPLS service. Each entry in this table provides LDP specific information for the VPlS represented by cvplsConfigIndex.')
cvplsLdpPwBindMacAddressLimit = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 141, 1, 2, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cvplsLdpPwBindMacAddressLimit.setStatus('current')
if mibBuilder.loadTexts: cvplsLdpPwBindMacAddressLimit.setDescription('The value of this object specifies the maximum number of learned and static entries allowed in the Forwarding database for this PW Binding. The value 0 means there is no limit for this PW Binding.')
cvplsLdpCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 141, 2, 1))
cvplsLdpModuleFullCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 10, 141, 2, 1, 1)).setObjects(("CISCO-IETF-VPLS-LDP-MIB", "cvplsLdpGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cvplsLdpModuleFullCompliance = cvplsLdpModuleFullCompliance.setStatus('current')
if mibBuilder.loadTexts: cvplsLdpModuleFullCompliance.setDescription('Compliance requirement for implementations that provide full support for CISCO-IETF-VPLS-LDP-MIB. Such devices can then be monitored and configured using this MIB module.')
cvplsLdpModuleReadOnlyCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 10, 141, 2, 1, 2)).setObjects(("CISCO-IETF-VPLS-LDP-MIB", "cvplsLdpGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cvplsLdpModuleReadOnlyCompliance = cvplsLdpModuleReadOnlyCompliance.setStatus('current')
if mibBuilder.loadTexts: cvplsLdpModuleReadOnlyCompliance.setDescription('Compliance requirement for implementations that only provide read-only support for CISCO-IETF-VPLS-LDP-MIB. Such devices can then be monitored but cannot be configured using this MIB modules.')
cvplsLdpGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 141, 2, 2))
cvplsLdpGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 10, 141, 2, 2, 1)).setObjects(("CISCO-IETF-VPLS-LDP-MIB", "cvplsLdpConfigMacAddrWithdraw"), ("CISCO-IETF-VPLS-LDP-MIB", "cvplsLdpPwBindMacAddressLimit"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cvplsLdpGroup = cvplsLdpGroup.setStatus('current')
if mibBuilder.loadTexts: cvplsLdpGroup.setDescription('The group of objects supporting management of L2VPN VPLS services using LDP.')
mibBuilder.exportSymbols("CISCO-IETF-VPLS-LDP-MIB", cvplsLdpGroups=cvplsLdpGroups, cvplsLdpConfigMacAddrWithdraw=cvplsLdpConfigMacAddrWithdraw, cvplsLdpMIB=cvplsLdpMIB, cvplsLdpConfigTable=cvplsLdpConfigTable, cvplsLdpPwBindMacAddressLimit=cvplsLdpPwBindMacAddressLimit, cvplsLdpGroup=cvplsLdpGroup, cvplsLdpObjects=cvplsLdpObjects, cvplsLdpPwBindTable=cvplsLdpPwBindTable, cvplsLdpModuleFullCompliance=cvplsLdpModuleFullCompliance, PYSNMP_MODULE_ID=cvplsLdpMIB, cvplsLdpConformance=cvplsLdpConformance, cvplsLdpPwBindEntry=cvplsLdpPwBindEntry, cvplsLdpConfigEntry=cvplsLdpConfigEntry, cvplsLdpCompliances=cvplsLdpCompliances, cvplsLdpModuleReadOnlyCompliance=cvplsLdpModuleReadOnlyCompliance)
