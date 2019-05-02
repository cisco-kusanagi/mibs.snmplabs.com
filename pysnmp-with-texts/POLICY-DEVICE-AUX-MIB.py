#
# PySNMP MIB module POLICY-DEVICE-AUX-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/POLICY-DEVICE-AUX-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:41:12 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
experimental, iso, MibIdentifier, IpAddress, TimeTicks, Gauge32, ModuleIdentity, Counter32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, Integer32, Unsigned32, Bits, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "experimental", "iso", "MibIdentifier", "IpAddress", "TimeTicks", "Gauge32", "ModuleIdentity", "Counter32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "Integer32", "Unsigned32", "Bits", "Counter64")
RowStatus, TextualConvention, StorageType, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "TextualConvention", "StorageType", "DisplayString")
policyDeviceAuxMib = ModuleIdentity((1, 3, 6, 1, 3, 999))
if mibBuilder.loadTexts: policyDeviceAuxMib.setLastUpdated('200007121800Z')
if mibBuilder.loadTexts: policyDeviceAuxMib.setOrganization('IETF RAP WG')
if mibBuilder.loadTexts: policyDeviceAuxMib.setContactInfo('Kwok Ho Chan Nortel Networks, Inc. 600 Technology Park Drive Billerica, MA 01821 USA Phone: +1 978 288 8175 Email: khchan@nortelnetworks.com John Seligson Nortel Networks, Inc. 4401 Great America Parkway Santa Clara, CA USA 95054 Phone: +1 408 495-2992 Email: jseligso@nortelnetworks.com Keith McCloghrie Cisco Systems, Inc. 170 West Tasman Drive, San Jose, CA 95134-1706 USA Phone: +1 408 526 5260 Email: kzm@cisco.com')
if mibBuilder.loadTexts: policyDeviceAuxMib.setDescription('This module defines an infrastructure used for support of policy-based provisioning of a network device.')
policyDeviceAuxObjects = MibIdentifier((1, 3, 6, 1, 3, 999, 1))
policyDeviceAuxConformance = MibIdentifier((1, 3, 6, 1, 3, 999, 2))
policyDeviceConfig = MibIdentifier((1, 3, 6, 1, 3, 999, 1, 1))
class Role(TextualConvention, OctetString):
    reference = 'Policy Core Information Model, draft-ietf-policy-core-info-model-06.txt'
    description = 'A role represents a functionality characteristic or capability of a resource to which policies are applied. Examples of roles include Backbone interface, Frame Relay interface, BGP-capable router, web server, firewall, etc. Valid characters are a-z, A-Z, 0-9, period, hyphen and underscore. A role must not start with an underscore.'
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(1, 31)

class RoleCombination(TextualConvention, OctetString):
    description = "A Display string consisting of a set of roles concatenated with a '+' character where the roles are in lexicographic order from minimum to maximum. For example, a+b and b+a are NOT different role-combinations; rather, they are different formating of the same (one) role- combination. Notice the roles within a role-combination are in lexicographic order from minimum to maximum, hence, we declare: a+b is the valid formating of the role-combination, b+a is an invalid formating of the role-combination. Notice the need of zero-length role-combination as the role- combination of interfaces to which no roles have been assigned. This role-combination is also known as the null role-combination. (Note the deliberate use of lower case leters to avoid confusion with the ASCII NULL character which has a value of zero but length of one.)"
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 255)

policyInterfaceTable = MibTable((1, 3, 6, 1, 3, 999, 1, 1, 1), )
if mibBuilder.loadTexts: policyInterfaceTable.setStatus('current')
if mibBuilder.loadTexts: policyInterfaceTable.setDescription("Policy information about a device's interfaces.")
policyInterfaceEntry = MibTableRow((1, 3, 6, 1, 3, 999, 1, 1, 1, 1), ).setIndexNames((0, "POLICY-DEVICE-AUX-MIB", "policyInterfaceIfIndex"))
if mibBuilder.loadTexts: policyInterfaceEntry.setStatus('current')
if mibBuilder.loadTexts: policyInterfaceEntry.setDescription('A conceptual row in the policyInterfaceTable. Each row identifies policy infromation about a particular interface.')
policyInterfaceIfIndex = MibTableColumn((1, 3, 6, 1, 3, 999, 1, 1, 1, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: policyInterfaceIfIndex.setStatus('current')
if mibBuilder.loadTexts: policyInterfaceIfIndex.setDescription('The ifIndex value for which this conceptual row provides policy information.')
policyInterfaceRoleCombo = MibTableColumn((1, 3, 6, 1, 3, 999, 1, 1, 1, 1, 2), RoleCombination()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: policyInterfaceRoleCombo.setStatus('current')
if mibBuilder.loadTexts: policyInterfaceRoleCombo.setDescription('The role combination that is associated with this interface for the purpose of assigning policies to this interface.')
policyInterfaceStorage = MibTableColumn((1, 3, 6, 1, 3, 999, 1, 1, 1, 1, 3), StorageType().clone('volatile')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: policyInterfaceStorage.setStatus('current')
if mibBuilder.loadTexts: policyInterfaceStorage.setDescription('The storage type for this conceptual row. Conceptual rows having the value permanent(4) need not allow write-access to any columnar objects in the row. This object may not be modified if the associated policyInterfaceStatus object is equal to active(1).')
policyInterfaceStatus = MibTableColumn((1, 3, 6, 1, 3, 999, 1, 1, 1, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: policyInterfaceStatus.setStatus('current')
if mibBuilder.loadTexts: policyInterfaceStatus.setDescription('The status of this row. An entry may not exist in the active state unless all objects in the entry have an appropriate value. Row creation using only default values is supported.')
policyDeviceCompliances = MibIdentifier((1, 3, 6, 1, 3, 999, 2, 1))
policyDeviceGroups = MibIdentifier((1, 3, 6, 1, 3, 999, 2, 2))
policyDeviceCompliance = ModuleCompliance((1, 3, 6, 1, 3, 999, 2, 1, 1)).setObjects(("POLICY-DEVICE-AUX-MIB", "policyInterfaceGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    policyDeviceCompliance = policyDeviceCompliance.setStatus('current')
if mibBuilder.loadTexts: policyDeviceCompliance.setDescription('Describes the requirements for conformance to the Policy Auxiliary MIB.')
policyInterfaceGroup = ObjectGroup((1, 3, 6, 1, 3, 999, 2, 2, 1)).setObjects(("POLICY-DEVICE-AUX-MIB", "policyInterfaceRoleCombo"), ("POLICY-DEVICE-AUX-MIB", "policyInterfaceStorage"), ("POLICY-DEVICE-AUX-MIB", "policyInterfaceStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    policyInterfaceGroup = policyInterfaceGroup.setStatus('current')
if mibBuilder.loadTexts: policyInterfaceGroup.setDescription('Objects used to define interface to role combination mappings.')
mibBuilder.exportSymbols("POLICY-DEVICE-AUX-MIB", policyInterfaceRoleCombo=policyInterfaceRoleCombo, Role=Role, policyInterfaceStatus=policyInterfaceStatus, policyDeviceConfig=policyDeviceConfig, policyInterfaceEntry=policyInterfaceEntry, policyInterfaceGroup=policyInterfaceGroup, policyDeviceCompliance=policyDeviceCompliance, RoleCombination=RoleCombination, policyDeviceAuxConformance=policyDeviceAuxConformance, policyDeviceAuxMib=policyDeviceAuxMib, policyInterfaceIfIndex=policyInterfaceIfIndex, policyInterfaceStorage=policyInterfaceStorage, policyDeviceGroups=policyDeviceGroups, policyDeviceAuxObjects=policyDeviceAuxObjects, policyDeviceCompliances=policyDeviceCompliances, policyInterfaceTable=policyInterfaceTable, PYSNMP_MODULE_ID=policyDeviceAuxMib)
