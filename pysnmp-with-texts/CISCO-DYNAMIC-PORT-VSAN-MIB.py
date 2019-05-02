#
# PySNMP MIB module CISCO-DYNAMIC-PORT-VSAN-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-DYNAMIC-PORT-VSAN-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:56:27 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint")
CpsmActivateResult, CpsmDiffDb, CpsmDbActivate, CpsmDiffReason = mibBuilder.importSymbols("CISCO-PSM-MIB", "CpsmActivateResult", "CpsmDiffDb", "CpsmDbActivate", "CpsmDiffReason")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
VsanIndex, FcNameIdOrZero, FcNameId = mibBuilder.importSymbols("CISCO-ST-TC", "VsanIndex", "FcNameIdOrZero", "FcNameId")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
TimeTicks, Counter32, Gauge32, MibIdentifier, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, Unsigned32, iso, Counter64, ModuleIdentity, Bits, Integer32, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "Counter32", "Gauge32", "MibIdentifier", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "Unsigned32", "iso", "Counter64", "ModuleIdentity", "Bits", "Integer32", "NotificationType")
RowStatus, TextualConvention, DisplayString, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "TextualConvention", "DisplayString", "TruthValue")
ciscoDpvmMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 421))
ciscoDpvmMIB.setRevisions(('2004-06-22 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoDpvmMIB.setRevisionsDescriptions(('Initial version of this MIB.',))
if mibBuilder.loadTexts: ciscoDpvmMIB.setLastUpdated('200406220000Z')
if mibBuilder.loadTexts: ciscoDpvmMIB.setOrganization('Cisco Systems Inc.')
if mibBuilder.loadTexts: ciscoDpvmMIB.setContactInfo(' Cisco Systems Customer Service Postal: 170 W Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-san@cisco.com')
if mibBuilder.loadTexts: ciscoDpvmMIB.setDescription('The MIB module for the management of the Dynamic Port Vsan Membership (DPVM) module. DPVM provides the ability to assign (virtual storage area network) VSAN IDs dynamically to switch ports based on the device logging in on the port. The logging-in device can be identified by its port World Wide Name (pWWN) and/or its node World Wide Name (nWWN).')
ciscoDpvmMIBNotifs = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 421, 0))
ciscoDpvmMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 421, 1))
ciscoDpvmMIBConform = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 421, 2))
cdpvmConfiguration = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 421, 1, 1))
class CdpvmDevType(TextualConvention, Integer32):
    description = 'Represents the type of device. pwwn(1) - Represents the port WWN of the device. nwwn(2) - Represents the node WWN of the device.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("pwwn", 1), ("nwwn", 2))

cdpvmNextAvailIndex = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 421, 1, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 16384))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdpvmNextAvailIndex.setStatus('current')
if mibBuilder.loadTexts: cdpvmNextAvailIndex.setDescription('This object contains an appropriate value to be used for cdpvmIndex when creating entries in the cdpvmTable. The value 0 indicates that all entries are assigned. A management application should read this object, get the (non-zero) value and use same for creating an entry in the cdpvmTable. After each retrieval and use, the agent should modify the value to the next unassigned index. After a manager retrieves a value the agent will determine through its local policy when this index value will be made available for reuse. A suggested mechanism is to make an index available when the corresponding entry is deleted.')
cdpvmTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 421, 1, 1, 2), )
if mibBuilder.loadTexts: cdpvmTable.setStatus('current')
if mibBuilder.loadTexts: cdpvmTable.setDescription("This table contains the set of all valid bindings of devices to VSANs configured on the local device. A valid binding consists of a pWWN/nWWN bound to a VSAN. If a device is bound to a VSAN, then when that device logs in through a port on the local device, that port is assigned the configured VSAN. Such a VSAN is called a 'dynamic' VSAN. The set of valid bindings configured in this table should be activated by means of the cdpvmActivate object. When activated, these bindings are enforced and all subsequent logins will be subject to these bindings.")
cdpvmEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 421, 1, 1, 2, 1), ).setIndexNames((0, "CISCO-DYNAMIC-PORT-VSAN-MIB", "cdpvmIndex"))
if mibBuilder.loadTexts: cdpvmEntry.setStatus('current')
if mibBuilder.loadTexts: cdpvmEntry.setDescription('An entry (conceptual row) in this table. Each entry contains the mapping between a device and its dynamic VSAN.')
cdpvmIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 421, 1, 1, 2, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 16384)))
if mibBuilder.loadTexts: cdpvmIndex.setStatus('current')
if mibBuilder.loadTexts: cdpvmIndex.setDescription('Identifies a binding between a device and its dynamic VSAN.')
cdpvmLoginDevType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 421, 1, 1, 2, 1, 2), CdpvmDevType().clone('pwwn')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cdpvmLoginDevType.setStatus('current')
if mibBuilder.loadTexts: cdpvmLoginDevType.setDescription('Specifies the type of the corresponding instance of cdpvmLoginDev object.')
cdpvmLoginDev = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 421, 1, 1, 2, 1, 3), FcNameId()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cdpvmLoginDev.setStatus('current')
if mibBuilder.loadTexts: cdpvmLoginDev.setDescription("Represents the logging-in device. If the value of the corresponding instance of cdpvmLoginDevType is 'pwwn', then this object contains a pWWN. If the value of the corresponding instance of cdpvmLoginDevType is 'nwwn', then this object contains a nWWN. This object MUST be set to a valid value before or concurrently with setting the corresponding instance of cdpvmRowStatus to 'active'. The agent should not allow creation of 2 entries in this table with same values for cdpvmLoginDev and cdpvmLoginDevVsan.")
cdpvmLoginDevVsan = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 421, 1, 1, 2, 1, 4), VsanIndex().clone(1)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cdpvmLoginDevVsan.setStatus('current')
if mibBuilder.loadTexts: cdpvmLoginDevVsan.setDescription('Represents the VSAN to be associated to the port on the local device on which the device represented by cdpvmLoginDev logs in.')
cdpvmRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 421, 1, 1, 2, 1, 5), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cdpvmRowStatus.setStatus('current')
if mibBuilder.loadTexts: cdpvmRowStatus.setDescription("The status of this conceptual row. Before setting this object to 'active', the cdpvmLoginDev object MUST be set to a valid value. Only cdpvmLoginDevVsan object can be modified when the value of this object is 'active'.")
cdpvmActivate = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 421, 1, 1, 3), CpsmDbActivate()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cdpvmActivate.setStatus('current')
if mibBuilder.loadTexts: cdpvmActivate.setDescription("This object helps in activating the set of bindings in the cdpvmTable. Setting this object to 'activate(1)' will result in the valid bindings present in cdpvmTable being activated and copied to the cpdvmEnfTable. By default auto learn will be turned 'on' after activation. Before activation is attempted, it should be turned 'off'. Setting this object to 'forceActivate(3)', will result in forced activation, even if there are errors during activation and the activated bindings will be copied to the cdpvmEnfTable. Setting this object to 'deactivate(5)', will result in deactivation of currently activated valid bindings (if any). Currently active entries (if any), which would have been present in the cdpvmEnfTable, will be removed. Setting this object to 'activateWithAutoLearnOff(2)' and 'forceActivateWithAutoLearnOff(4)' is not allowed. Setting this object to 'noop(6)', results in no action. The value of this object when read is always 'noop(6)'. Activation will not be allowed if auto-learn is enabled.")
cdpvmActivateResult = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 421, 1, 1, 4), CpsmActivateResult()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdpvmActivateResult.setStatus('current')
if mibBuilder.loadTexts: cdpvmActivateResult.setDescription('This object indicates the outcome of the activation.')
cdpvmAutoLearn = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 421, 1, 1, 5), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cdpvmAutoLearn.setStatus('current')
if mibBuilder.loadTexts: cdpvmAutoLearn.setDescription("This object helps to 'learn' the configuration of devices logged into the local device on all its ports and the VSANs to which they are associated. This information will be populated in the the enforced binding table (cdpvmEnfTable). This mechanism of 'learning' the configuration of devices and their VSAN association over a period of time and populating the configuration is a convenience mechanism for users. If this object is set to 'true(1)' all subsequent logins and their VSAN association will be populated in the enforced binding database, provided it is not in conflict with existing enforced bindings. When this object is set to 'false(2)', the mechanism of learning is stopped. The learned entries will however be in the enforced binding database.")
cdpvmCopyEnfToConfig = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 421, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("copy", 1), ("noop", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cdpvmCopyEnfToConfig.setStatus('current')
if mibBuilder.loadTexts: cdpvmCopyEnfToConfig.setDescription("This object when set to 'copy(1)', results in the active (enforced) binding database to be copied on to the configuration binding database. Note that the learned entries are also copied. No action is taken if this object is set to 'noop(2)'. The value of this object when read is always 'noop'.")
cdpvmEnfTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 421, 1, 1, 7), )
if mibBuilder.loadTexts: cdpvmEnfTable.setStatus('current')
if mibBuilder.loadTexts: cdpvmEnfTable.setDescription('This table contains information on all currently enforced bindings on the local device. The enforced set of bindings is the set of valid bindings copied from the configuration binding database (cdpvmTable) at the time they were activated. These entries cannot be modified. The learnt entries are also a part of this table. Entries can get into this table or be deleted from this table only by means of explicit activation/deactivation. Note that this table will be empty when no valid bindings have been activated.')
cdpvmEnfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 421, 1, 1, 7, 1), ).setIndexNames((0, "CISCO-DYNAMIC-PORT-VSAN-MIB", "cdpvmEnfIndex"))
if mibBuilder.loadTexts: cdpvmEnfEntry.setStatus('current')
if mibBuilder.loadTexts: cdpvmEnfEntry.setDescription('An entry (conceptual row) in this table.')
cdpvmEnfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 421, 1, 1, 7, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 16384)))
if mibBuilder.loadTexts: cdpvmEnfIndex.setStatus('current')
if mibBuilder.loadTexts: cdpvmEnfIndex.setDescription('The index of this entry.')
cdpvmEnfLoginDevType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 421, 1, 1, 7, 1, 2), CdpvmDevType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdpvmEnfLoginDevType.setStatus('current')
if mibBuilder.loadTexts: cdpvmEnfLoginDevType.setDescription('Specifies the type of the corresponding instance of cdpvmEnfLoginDev.')
cdpvmEnfLoginDev = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 421, 1, 1, 7, 1, 3), FcNameId()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdpvmEnfLoginDev.setStatus('current')
if mibBuilder.loadTexts: cdpvmEnfLoginDev.setDescription('This object represents the logging in device address. This object was copied from the cdpvmLoginDev object in the cdpvmTable at the time when the currently active bindings were activated.')
cdpvmEnfLoginDevVsan = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 421, 1, 1, 7, 1, 4), VsanIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdpvmEnfLoginDevVsan.setStatus('current')
if mibBuilder.loadTexts: cdpvmEnfLoginDevVsan.setDescription("This object represents the VSAN of the port on the local device thru' which the device represented by cdpvmEnfLoginDev logs in. This object was copied from the cdpvmLoginDevVsan object in the cdpvmTable at the time when the currently active bindings were activated")
cdpvmEnfIsLearnt = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 421, 1, 1, 7, 1, 5), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdpvmEnfIsLearnt.setStatus('current')
if mibBuilder.loadTexts: cdpvmEnfIsLearnt.setDescription("This object indicates if this is a learnt entry or not. If the value of this object is 'true', then it is a learnt entry. If the value of this object is 'false', then it is not.")
cdpvmDynPortsTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 421, 1, 1, 8), )
if mibBuilder.loadTexts: cdpvmDynPortsTable.setStatus('current')
if mibBuilder.loadTexts: cdpvmDynPortsTable.setDescription('This table contains the set of all ports that are operating with a dynamic VSAN on the local device.')
cdpvmDynPortsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 421, 1, 1, 8, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: cdpvmDynPortsEntry.setStatus('current')
if mibBuilder.loadTexts: cdpvmDynPortsEntry.setDescription('An entry (conceptual row) in this table.')
cdpvmDynPortVsan = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 421, 1, 1, 8, 1, 1), VsanIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdpvmDynPortVsan.setStatus('current')
if mibBuilder.loadTexts: cdpvmDynPortVsan.setDescription("The 'dynamic' VSAN of this port on the local device.")
cdpvmDynPortDevPwwn = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 421, 1, 1, 8, 1, 2), FcNameId()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdpvmDynPortDevPwwn.setStatus('current')
if mibBuilder.loadTexts: cdpvmDynPortDevPwwn.setDescription('The pWWN of the device currently logged-in through this port on the local device.')
cdpvmDynPortDevNwwn = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 421, 1, 1, 8, 1, 3), FcNameId()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdpvmDynPortDevNwwn.setStatus('current')
if mibBuilder.loadTexts: cdpvmDynPortDevNwwn.setDescription("The nWWN of the device currently logged-in thru' this port on the local device.")
cdpvmDiffConfig = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 421, 1, 1, 9), CpsmDiffDb()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cdpvmDiffConfig.setStatus('current')
if mibBuilder.loadTexts: cdpvmDiffConfig.setDescription("The config database represented by cdpvmTable and the enforced database represented by cdpvmEnfTable can be compared to list out the differences. This object specifies the reference database for the comparison. This object when set to 'configDb(1)', compares the configuration database (cdpvmTable) with respect to the enforced database (cdpvmEnfTable). So, the enforced database will be the reference database and the results of comparison operation will be with respect to the enforced database. This object when set to 'activeDb(2)', compares the enforced database with respect to the configuration database. So, the configured database will be the reference database and the results of comparison operation will be with respect to the configuration database. No action will be taken if this object is set to 'noop(3)'. The value of this object when read is always 'noop(3)'.")
cdpvmDiffTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 421, 1, 1, 10), )
if mibBuilder.loadTexts: cdpvmDiffTable.setStatus('current')
if mibBuilder.loadTexts: cdpvmDiffTable.setDescription('This table contains the result of the compare operation configured by means of the cdpvmDiffConfig object.')
cdpvmDiffEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 421, 1, 1, 10, 1), ).setIndexNames((0, "CISCO-DYNAMIC-PORT-VSAN-MIB", "cdpvmDiffIndex"))
if mibBuilder.loadTexts: cdpvmDiffEntry.setStatus('current')
if mibBuilder.loadTexts: cdpvmDiffEntry.setDescription('An entry (conceptual row) in this table.')
cdpvmDiffIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 421, 1, 1, 10, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 16384)))
if mibBuilder.loadTexts: cdpvmDiffIndex.setStatus('current')
if mibBuilder.loadTexts: cdpvmDiffIndex.setDescription('The index of this entry.')
cdpvmDiffReason = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 421, 1, 1, 10, 1, 2), CpsmDiffReason()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdpvmDiffReason.setStatus('current')
if mibBuilder.loadTexts: cdpvmDiffReason.setDescription('This object indicates the reason for the difference between the databases being compared, for this entry.')
cdpvmDiffLoginDevType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 421, 1, 1, 10, 1, 3), CdpvmDevType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdpvmDiffLoginDevType.setStatus('current')
if mibBuilder.loadTexts: cdpvmDiffLoginDevType.setDescription('Specifies the type of the corresponding instance of cdpvmDiffLoginDev object.')
cdpvmDiffLoginDev = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 421, 1, 1, 10, 1, 4), FcNameId()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdpvmDiffLoginDev.setStatus('current')
if mibBuilder.loadTexts: cdpvmDiffLoginDev.setDescription('This object represents the logging-in device address. This object was copied from either the cdpvmLoginDev object in the cdpvmTable or from cdpvmEnfLoginDev object in the cdpvmEnfTable at the time when the comparison was done.')
cdpvmDiffLoginDevVsan = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 421, 1, 1, 10, 1, 5), VsanIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdpvmDiffLoginDevVsan.setStatus('current')
if mibBuilder.loadTexts: cdpvmDiffLoginDevVsan.setDescription("This object represents the VSAN of the port on the local device thru' which the device represented by the corresponding instance of cdpvmDiffLoginDev object, logged-in. It was copied from either the cdpvmLoginDevVsan object in the cdpvmTable or from cdpvmEnfLoginDevVsan object in the cdpvmEnfTable at the time when the comparison was done.")
cdpvmClearAutoLearn = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 421, 1, 1, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("clear", 1), ("clearOnWwn", 2), ("noop", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cdpvmClearAutoLearn.setStatus('current')
if mibBuilder.loadTexts: cdpvmClearAutoLearn.setDescription("This object assists in clearing the auto-learnt entries. Setting this object to 'clear(1)' will result in all auto-learnt entries being cleared. Setting this object to 'clearOnWwn(2)' will result in a particular entry represented by cdpvmClearAutoLearnWwn object being cleared. Before setting this object to 'clearOnWwn(2)', the cpdvmClearAutoLearnWwn object should be set to the pWWN that is to be cleared. Setting this object to 'noop(3)', will result in no action being taken. The value of this object when read is always 'noop'.")
cdpvmClearAutoLearnWwn = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 421, 1, 1, 12), FcNameIdOrZero().clone(hexValue="")).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cdpvmClearAutoLearnWwn.setStatus('current')
if mibBuilder.loadTexts: cdpvmClearAutoLearnWwn.setDescription('Represents the port WWN (pWWN) to be used for clearing its corresponding auto-learnt entry.')
cdpvmActivationState = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 421, 1, 1, 13), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdpvmActivationState.setStatus('current')
if mibBuilder.loadTexts: cdpvmActivationState.setDescription("This object indicates the state of activation. If the value of this object is 'true', then an activation has been attempted as the most recent operation. If the value of this object is 'false', then an activation has not been attempted as the most recent operation.")
ciscoDpvmMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 421, 2, 1))
ciscoDpvmMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 421, 2, 2))
ciscoDpvmMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 421, 2, 1, 1)).setObjects(("CISCO-DYNAMIC-PORT-VSAN-MIB", "ciscoDpvmConfigGroup"), ("CISCO-DYNAMIC-PORT-VSAN-MIB", "ciscoDpvmEnforcedGroup"), ("CISCO-DYNAMIC-PORT-VSAN-MIB", "ciscoDpvmAutoLearnGroup"), ("CISCO-DYNAMIC-PORT-VSAN-MIB", "ciscoDpvmDiffGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoDpvmMIBCompliance = ciscoDpvmMIBCompliance.setStatus('current')
if mibBuilder.loadTexts: ciscoDpvmMIBCompliance.setDescription('The compliance statement for entities which implement the Dynamic Port VSAN Membership Manager.')
ciscoDpvmConfigGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 421, 2, 2, 1)).setObjects(("CISCO-DYNAMIC-PORT-VSAN-MIB", "cdpvmNextAvailIndex"), ("CISCO-DYNAMIC-PORT-VSAN-MIB", "cdpvmLoginDevType"), ("CISCO-DYNAMIC-PORT-VSAN-MIB", "cdpvmLoginDev"), ("CISCO-DYNAMIC-PORT-VSAN-MIB", "cdpvmLoginDevVsan"), ("CISCO-DYNAMIC-PORT-VSAN-MIB", "cdpvmRowStatus"), ("CISCO-DYNAMIC-PORT-VSAN-MIB", "cdpvmActivate"), ("CISCO-DYNAMIC-PORT-VSAN-MIB", "cdpvmActivateResult"), ("CISCO-DYNAMIC-PORT-VSAN-MIB", "cdpvmCopyEnfToConfig"), ("CISCO-DYNAMIC-PORT-VSAN-MIB", "cdpvmDynPortVsan"), ("CISCO-DYNAMIC-PORT-VSAN-MIB", "cdpvmDynPortDevPwwn"), ("CISCO-DYNAMIC-PORT-VSAN-MIB", "cdpvmDynPortDevNwwn"), ("CISCO-DYNAMIC-PORT-VSAN-MIB", "cdpvmActivationState"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoDpvmConfigGroup = ciscoDpvmConfigGroup.setStatus('current')
if mibBuilder.loadTexts: ciscoDpvmConfigGroup.setDescription('A set of objects for configuration of DPVM bindings.')
ciscoDpvmEnforcedGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 421, 2, 2, 2)).setObjects(("CISCO-DYNAMIC-PORT-VSAN-MIB", "cdpvmEnfLoginDevType"), ("CISCO-DYNAMIC-PORT-VSAN-MIB", "cdpvmEnfLoginDev"), ("CISCO-DYNAMIC-PORT-VSAN-MIB", "cdpvmEnfLoginDevVsan"), ("CISCO-DYNAMIC-PORT-VSAN-MIB", "cdpvmEnfIsLearnt"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoDpvmEnforcedGroup = ciscoDpvmEnforcedGroup.setStatus('current')
if mibBuilder.loadTexts: ciscoDpvmEnforcedGroup.setDescription('A set of objects for displaying enforced DPVM bindings.')
ciscoDpvmAutoLearnGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 421, 2, 2, 3)).setObjects(("CISCO-DYNAMIC-PORT-VSAN-MIB", "cdpvmAutoLearn"), ("CISCO-DYNAMIC-PORT-VSAN-MIB", "cdpvmClearAutoLearn"), ("CISCO-DYNAMIC-PORT-VSAN-MIB", "cdpvmClearAutoLearnWwn"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoDpvmAutoLearnGroup = ciscoDpvmAutoLearnGroup.setStatus('current')
if mibBuilder.loadTexts: ciscoDpvmAutoLearnGroup.setDescription('A set of object(s) for configuring auto-learn of DPVM bindings.')
ciscoDpvmDiffGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 421, 2, 2, 4)).setObjects(("CISCO-DYNAMIC-PORT-VSAN-MIB", "cdpvmDiffConfig"), ("CISCO-DYNAMIC-PORT-VSAN-MIB", "cdpvmDiffReason"), ("CISCO-DYNAMIC-PORT-VSAN-MIB", "cdpvmDiffLoginDevType"), ("CISCO-DYNAMIC-PORT-VSAN-MIB", "cdpvmDiffLoginDev"), ("CISCO-DYNAMIC-PORT-VSAN-MIB", "cdpvmDiffLoginDevVsan"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoDpvmDiffGroup = ciscoDpvmDiffGroup.setStatus('current')
if mibBuilder.loadTexts: ciscoDpvmDiffGroup.setDescription('A set of objects for configuring and displaying database compare operations.')
mibBuilder.exportSymbols("CISCO-DYNAMIC-PORT-VSAN-MIB", cdpvmDynPortDevPwwn=cdpvmDynPortDevPwwn, cdpvmTable=cdpvmTable, ciscoDpvmMIBCompliance=ciscoDpvmMIBCompliance, cdpvmNextAvailIndex=cdpvmNextAvailIndex, cdpvmDynPortsTable=cdpvmDynPortsTable, cdpvmDiffTable=cdpvmDiffTable, ciscoDpvmMIBObjects=ciscoDpvmMIBObjects, cdpvmDiffLoginDev=cdpvmDiffLoginDev, cdpvmLoginDev=cdpvmLoginDev, ciscoDpvmMIBCompliances=ciscoDpvmMIBCompliances, cdpvmDynPortDevNwwn=cdpvmDynPortDevNwwn, cdpvmLoginDevType=cdpvmLoginDevType, cdpvmDiffIndex=cdpvmDiffIndex, cdpvmDiffConfig=cdpvmDiffConfig, ciscoDpvmMIBNotifs=ciscoDpvmMIBNotifs, cdpvmCopyEnfToConfig=cdpvmCopyEnfToConfig, cdpvmActivate=cdpvmActivate, cdpvmActivateResult=cdpvmActivateResult, PYSNMP_MODULE_ID=ciscoDpvmMIB, cdpvmDiffLoginDevType=cdpvmDiffLoginDevType, cdpvmEntry=cdpvmEntry, cdpvmClearAutoLearnWwn=cdpvmClearAutoLearnWwn, cdpvmLoginDevVsan=cdpvmLoginDevVsan, cdpvmEnfEntry=cdpvmEnfEntry, ciscoDpvmMIB=ciscoDpvmMIB, cdpvmEnfLoginDevType=cdpvmEnfLoginDevType, cdpvmAutoLearn=cdpvmAutoLearn, cdpvmEnfLoginDevVsan=cdpvmEnfLoginDevVsan, ciscoDpvmDiffGroup=ciscoDpvmDiffGroup, cdpvmRowStatus=cdpvmRowStatus, cdpvmDiffEntry=cdpvmDiffEntry, cdpvmEnfIsLearnt=cdpvmEnfIsLearnt, ciscoDpvmMIBConform=ciscoDpvmMIBConform, cdpvmDynPortsEntry=cdpvmDynPortsEntry, cdpvmEnfLoginDev=cdpvmEnfLoginDev, cdpvmClearAutoLearn=cdpvmClearAutoLearn, ciscoDpvmEnforcedGroup=ciscoDpvmEnforcedGroup, ciscoDpvmMIBGroups=ciscoDpvmMIBGroups, cdpvmDiffReason=cdpvmDiffReason, cdpvmEnfIndex=cdpvmEnfIndex, cdpvmDiffLoginDevVsan=cdpvmDiffLoginDevVsan, ciscoDpvmAutoLearnGroup=ciscoDpvmAutoLearnGroup, cdpvmConfiguration=cdpvmConfiguration, ciscoDpvmConfigGroup=ciscoDpvmConfigGroup, cdpvmDynPortVsan=cdpvmDynPortVsan, CdpvmDevType=CdpvmDevType, cdpvmActivationState=cdpvmActivationState, cdpvmEnfTable=cdpvmEnfTable, cdpvmIndex=cdpvmIndex)
