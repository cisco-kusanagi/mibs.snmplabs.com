#
# PySNMP MIB module CTRON-SMARTTRUNK-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CTRON-SMARTTRUNK-MIB
# Produced by pysmi-0.3.4 at Wed May  1 12:31:19 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection")
ctSmartTrunkBranch, = mibBuilder.importSymbols("CTRON-MIB-NAMES", "ctSmartTrunkBranch")
InterfaceIndex, ifIndex = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex", "ifIndex")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
ModuleIdentity, ObjectIdentity, iso, Bits, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, TimeTicks, Gauge32, NotificationType, Unsigned32, MibIdentifier, Counter64, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "ObjectIdentity", "iso", "Bits", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "TimeTicks", "Gauge32", "NotificationType", "Unsigned32", "MibIdentifier", "Counter64", "Integer32")
DisplayString, RowStatus, TruthValue, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "RowStatus", "TruthValue", "TextualConvention")
ctSmartTrunk = ModuleIdentity((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 20, 1))
if mibBuilder.loadTexts: ctSmartTrunk.setLastUpdated('199812160000Z')
if mibBuilder.loadTexts: ctSmartTrunk.setOrganization('Cabletron Systems, Inc')
if mibBuilder.loadTexts: ctSmartTrunk.setContactInfo('Cabletron Systems, Inc. 35 Industrial Way, P.O. Box 5005 Rochester, NH 03867-0505 (603) 332-9400 support@cabletron.com http://www.ctron.com')
if mibBuilder.loadTexts: ctSmartTrunk.setDescription('This mib module defines a portion of the SNMP enterprise MIBs under Cabletron enterprise OID pertaining to configuration of Smart TRUNK network links.')
ctSmartTrunkConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 20, 1, 1))
ctSmartTrunkDebug = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 20, 1, 2))
class CTSmartTrunkProtocol(TextualConvention, Integer32):
    description = 'Type of trunking protocol used. LLAP based switches should use decHuntGroup. noProcol applies to all other types of connections.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("noProtocol", 1), ("decHuntGroup", 2))

class CTSmartTrunkIndex(TextualConvention, Integer32):
    description = "Most of the tables in this MIB are indexed in whole or in part by 'ctTrunkIndex' - not by 'ifIndex'. Why is there a separate index? Traditionally, ifIndex values are chosen by agents, and are permitted to change across restarts. Using ifIndex to index ctTrunkConfigTable could complicate row creation and/or cause interoperability problems (if each agent had special restrictions on ifIndex). Having a separate index avoids these problems."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 2147483647)

class CTSmartTrunkName(DisplayString):
    description = 'A textual description of this virtual port.'
    status = 'current'
    subtypeSpec = DisplayString.subtypeSpec + ValueSizeConstraint(0, 32)

class CTSmartTrunkLoadBalanceType(TextualConvention, Integer32):
    description = 'The algorithm in use to assign flows to each link in a Smart TRUNK.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("balancingUnspecified", 1), ("roundRobin", 2), ("linkUtilization", 3))

ctTrunkGlobalStatus = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 20, 1, 1, 1), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctTrunkGlobalStatus.setStatus('current')
if mibBuilder.loadTexts: ctTrunkGlobalStatus.setDescription('The state of Smart TRUNK capability for this entire managed entity. Default Value is True(1). If set to False(2) all smart trunks are put into ifAdminStatus down.')
ctTrunkConfigTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 20, 1, 1, 3), )
if mibBuilder.loadTexts: ctTrunkConfigTable.setStatus('current')
if mibBuilder.loadTexts: ctTrunkConfigTable.setDescription("A table describing all of the trunk interfaces implemented by this host. Each trunk has a row in the MIB-II/RFC 2233 Interfaces table (describing the structure of the trunk interface it presents to higher layers). Each trunk interface also has a row in this and other CTRON-SMARTTRUNK-MIB tables. Smart Trunks use ifType propMultiplexor(54). Counters represent the aggregate of all physcal links. Unlike hardware ports, trunk interfaces can be created by management. However, the RFC 2233 Interfaces table does not directly support row creation. Therefore, creating or deleting a row in the ctTrunkConfigTable is defined to have the side effect of creating or deleting corresponding rows in - the MIB-II / RFC 2233 Interfaces table, - any other dependent tables New Interfaces table rows for trunk intefaces always have 'ifAdminStatus' set to 'down' until the row state is becomes Active. Then administration of the interface uses normal ifTable ifAdminStatus to enabled it.")
ctTrunkConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 20, 1, 1, 3, 1), ).setIndexNames((0, "CTRON-SMARTTRUNK-MIB", "ctTrunkIndex"))
if mibBuilder.loadTexts: ctTrunkConfigEntry.setStatus('current')
if mibBuilder.loadTexts: ctTrunkConfigEntry.setDescription('Each table entry contains configuration information for one trunk interface.')
ctTrunkIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 20, 1, 1, 3, 1, 1), CTSmartTrunkIndex())
if mibBuilder.loadTexts: ctTrunkIndex.setStatus('current')
if mibBuilder.loadTexts: ctTrunkIndex.setDescription('A value which uniquely identifies this conceptual row in the ctTrunkConfigTable. The Table allows sparse values. If the conceptual row identified by this value of ctTrunkIndex is recreated following an agent restart, the same value of ctTrunkIndex must be used to identify the recreated row. (However, the Interfaces table index associated with the client may change. ifAlias in ifXTable is used then to reassociate ifIndexes based on ifAlias. In the case of the SSR, Smart Trunks are manipulated as st.ctTrunkIndex')
ctTrunkConfigName = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 20, 1, 1, 3, 1, 2), CTSmartTrunkName()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ctTrunkConfigName.setStatus('current')
if mibBuilder.loadTexts: ctTrunkConfigName.setDescription("The Trunk's Name, just for informational purposes. It may be changed regardless of the RowStatus value.")
ctTrunkConfigProtocol = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 20, 1, 1, 3, 1, 3), CTSmartTrunkProtocol().clone('decHuntGroup')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ctTrunkConfigProtocol.setStatus('current')
if mibBuilder.loadTexts: ctTrunkConfigProtocol.setDescription('Trunking protocol in use. Once the row is active, it can not be changed.')
ctTrunkConfigLoadBalance = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 20, 1, 1, 3, 1, 4), CTSmartTrunkLoadBalanceType().clone('balancingUnspecified')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ctTrunkConfigLoadBalance.setStatus('current')
if mibBuilder.loadTexts: ctTrunkConfigLoadBalance.setDescription('The type of load balance algorithm applied to this trunk. Once Row is active, the agent may override this value with an implmentation specific default.')
ctTrunkIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 20, 1, 1, 3, 1, 5), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctTrunkIfIndex.setStatus('current')
if mibBuilder.loadTexts: ctTrunkIfIndex.setDescription('The ifIndex in ifTable, ifXTable that is associated with the trunk that is represented by this row.')
ctTrunkRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 20, 1, 1, 3, 1, 6), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ctTrunkRowStatus.setStatus('current')
if mibBuilder.loadTexts: ctTrunkRowStatus.setDescription("This object lets network managers create and delete trunk interfaces, on systems that support this optional capability. It does not control the activation and deactivation of these interfaces; they are controlled by 'ifAdminStatus' in the ifTable. However, changing row state from active to notInService. will have the side effect of changing their 'ifAdminStatus' values to 'noPresent' or 'down', thus causing any active trunk connections to be terminated. When creating a trunk interface, it is up to the management station to determine a suitable 'ctTrunkIndex'. To facilitate interoperability, agents should not put any restrictions on the 'ctTrunkIndex' beyond the obvious ones that it be valid and unused. The Managed Objects that must be set in this table for a row to change from nonExistent/notReady to notInService/Active is simply an index. Ports can then be added to the Smart TRUNK via the ifStackTable. If you create a trunk interface via this object, it will initially have 'ifAdminStatus' = 'down' 'ifOperStatus' = 'down' when RowStatus is changed to active.")
ctTrunkConnectionTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 20, 1, 1, 4), )
if mibBuilder.loadTexts: ctTrunkConnectionTable.setStatus('current')
if mibBuilder.loadTexts: ctTrunkConnectionTable.setDescription('This table describes how local interfaces that are participating in a trunk are connected to remote interfaces. With this table, a management entity can determine that (for example) local interfaces 3, 4, and 6 are connected to remote interfaces 10, 17, and 19. This table is useful to debug configuration errors with remote devices. If ifAdminStatus/ifOperState is up, and no corresponding row is found in this table, then a management station can assume a the remote end does not have the decHuntGroup protocol active. Note: this entire table is read-only. Rows are created and deleted from this table as a side effect of trunks being created and deleted. Note: a managment entity could determine (for example) that interface 3 was participating in trunk 3 by using the ifStackTable and ctTrunkIfIndex.')
ctTrunkConnectionEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 20, 1, 1, 4, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: ctTrunkConnectionEntry.setStatus('current')
if mibBuilder.loadTexts: ctTrunkConnectionEntry.setDescription('Each table entry contains configuration information for one interface that is participating in a trunk.')
ctTrunkPortRemoteIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 20, 1, 1, 4, 1, 1), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctTrunkPortRemoteIfIndex.setStatus('current')
if mibBuilder.loadTexts: ctTrunkPortRemoteIfIndex.setDescription('The ifIndex of the interface at the other end of this part of the trunk link. If this value is 0, then for some reason there is no interface on the other side of this link. This might be a temporary condition or it might represent a real problem. Note: this table is indexed by ifIndex. So the index is the local ifIndex value and ctTrunkPortRemoteIfIndex is the remote ifIndex.')
ctTrunkLLAPRequirement = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 20, 1, 2, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("required", 1), ("notRequired", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctTrunkLLAPRequirement.setStatus('current')
if mibBuilder.loadTexts: ctTrunkLLAPRequirement.setDescription('Indicates whether this managed entity requires the LLAP updates to perform the trunking function. Certain families of products require LLAP (decHuntGroup Protocol) order for the Smart TRUNK functionality to work. A value of 1 implies that LLAP is necessary for smart-trunking to work on this platform, a value of 2 indicates that it is not necessary.')
ctTrunkMaxTrunks = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 20, 1, 2, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctTrunkMaxTrunks.setStatus('current')
if mibBuilder.loadTexts: ctTrunkMaxTrunks.setDescription('The maximum number of trunks that can be configured on this managed entity.')
ctTrunkFlowDiagnosticTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 20, 1, 2, 4), )
if mibBuilder.loadTexts: ctTrunkFlowDiagnosticTable.setStatus('current')
if mibBuilder.loadTexts: ctTrunkFlowDiagnosticTable.setDescription('Provide a means to programmatically evaluate the load balancing of a smart trunk. Assumes that load balancing is done on a flow by flow basis.')
ctTrunkFlowDiagnosticEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 20, 1, 2, 4, 1), ).setIndexNames((0, "CTRON-SMARTTRUNK-MIB", "ctTrunkIndex"), (0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: ctTrunkFlowDiagnosticEntry.setStatus('current')
if mibBuilder.loadTexts: ctTrunkFlowDiagnosticEntry.setDescription('Each row refers to a specific smart trunk and port within that smart trunk.')
ctTrunkFlowDiagnosticInstalledFlows = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 20, 1, 2, 4, 1, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctTrunkFlowDiagnosticInstalledFlows.setStatus('current')
if mibBuilder.loadTexts: ctTrunkFlowDiagnosticInstalledFlows.setDescription('A counter of the flows installed on this port since it was first operational.')
ctTrunkConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 20, 1, 3))
ctTrunkCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 20, 1, 3, 1))
ctTrunkGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 20, 1, 3, 2))
ctTrunkComplianceV10 = ModuleCompliance((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 20, 1, 3, 1, 1)).setObjects(("CTRON-SMARTTRUNK-MIB", "ctTrunkConfGroupV10"), ("CTRON-SMARTTRUNK-MIB", "ctTrunkFlowDiagnosticGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ctTrunkComplianceV10 = ctTrunkComplianceV10.setStatus('current')
if mibBuilder.loadTexts: ctTrunkComplianceV10.setDescription('The compliance statement for the CTRON-SMARTTRUNK-MIB.')
ctTrunkConfGroupV10 = ObjectGroup((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 20, 1, 3, 2, 1)).setObjects(("CTRON-SMARTTRUNK-MIB", "ctTrunkGlobalStatus"), ("CTRON-SMARTTRUNK-MIB", "ctTrunkRowStatus"), ("CTRON-SMARTTRUNK-MIB", "ctTrunkConfigName"), ("CTRON-SMARTTRUNK-MIB", "ctTrunkConfigProtocol"), ("CTRON-SMARTTRUNK-MIB", "ctTrunkConfigLoadBalance"), ("CTRON-SMARTTRUNK-MIB", "ctTrunkIfIndex"), ("CTRON-SMARTTRUNK-MIB", "ctTrunkPortRemoteIfIndex"), ("CTRON-SMARTTRUNK-MIB", "ctTrunkLLAPRequirement"), ("CTRON-SMARTTRUNK-MIB", "ctTrunkMaxTrunks"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ctTrunkConfGroupV10 = ctTrunkConfGroupV10.setStatus('current')
if mibBuilder.loadTexts: ctTrunkConfGroupV10.setDescription('A set of managed objects that make up version 1.0 of the CTRON-SMARTTRUNK-MIB.')
ctTrunkFlowDiagnosticGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 20, 1, 3, 2, 2)).setObjects(("CTRON-SMARTTRUNK-MIB", "ctTrunkFlowDiagnosticInstalledFlows"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ctTrunkFlowDiagnosticGroup = ctTrunkFlowDiagnosticGroup.setStatus('current')
if mibBuilder.loadTexts: ctTrunkFlowDiagnosticGroup.setDescription("A collection of diagnostic information related to interfaces participating in SmartTrunks; specifically to interfaces on devices that use 'flows'.")
mibBuilder.exportSymbols("CTRON-SMARTTRUNK-MIB", CTSmartTrunkName=CTSmartTrunkName, ctTrunkConfigTable=ctTrunkConfigTable, ctTrunkConformance=ctTrunkConformance, ctTrunkFlowDiagnosticEntry=ctTrunkFlowDiagnosticEntry, ctSmartTrunkDebug=ctSmartTrunkDebug, ctTrunkLLAPRequirement=ctTrunkLLAPRequirement, ctTrunkFlowDiagnosticTable=ctTrunkFlowDiagnosticTable, CTSmartTrunkIndex=CTSmartTrunkIndex, ctTrunkConfigProtocol=ctTrunkConfigProtocol, ctSmartTrunkConfig=ctSmartTrunkConfig, ctTrunkCompliances=ctTrunkCompliances, ctTrunkConfGroupV10=ctTrunkConfGroupV10, ctTrunkFlowDiagnosticGroup=ctTrunkFlowDiagnosticGroup, ctTrunkConfigLoadBalance=ctTrunkConfigLoadBalance, ctTrunkIndex=ctTrunkIndex, ctSmartTrunk=ctSmartTrunk, ctTrunkConnectionEntry=ctTrunkConnectionEntry, CTSmartTrunkProtocol=CTSmartTrunkProtocol, ctTrunkGlobalStatus=ctTrunkGlobalStatus, ctTrunkRowStatus=ctTrunkRowStatus, ctTrunkIfIndex=ctTrunkIfIndex, PYSNMP_MODULE_ID=ctSmartTrunk, ctTrunkGroups=ctTrunkGroups, ctTrunkConfigEntry=ctTrunkConfigEntry, CTSmartTrunkLoadBalanceType=CTSmartTrunkLoadBalanceType, ctTrunkMaxTrunks=ctTrunkMaxTrunks, ctTrunkConnectionTable=ctTrunkConnectionTable, ctTrunkComplianceV10=ctTrunkComplianceV10, ctTrunkFlowDiagnosticInstalledFlows=ctTrunkFlowDiagnosticInstalledFlows, ctTrunkConfigName=ctTrunkConfigName, ctTrunkPortRemoteIfIndex=ctTrunkPortRemoteIfIndex)
