#
# PySNMP MIB module TPLINK-ACL-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/TPLINK-ACL-MIB
# Produced by pysmi-0.3.4 at Wed May  1 15:24:10 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Unsigned32, Counter64, Counter32, Integer32, TimeTicks, Gauge32, Bits, ObjectIdentity, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "Counter64", "Counter32", "Integer32", "TimeTicks", "Gauge32", "Bits", "ObjectIdentity", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
tplinkMgmt, = mibBuilder.importSymbols("TPLINK-MIB", "tplinkMgmt")
TPRowStatus, = mibBuilder.importSymbols("TPLINK-TC-MIB", "TPRowStatus")
tplinkAclMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 11863, 6, 26))
tplinkAclMIB.setRevisions(('2012-12-13 09:30',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: tplinkAclMIB.setRevisionsDescriptions(('Initial version of this MIB module.',))
if mibBuilder.loadTexts: tplinkAclMIB.setLastUpdated('201212130930Z')
if mibBuilder.loadTexts: tplinkAclMIB.setOrganization('TPLINK')
if mibBuilder.loadTexts: tplinkAclMIB.setContactInfo(' www.tplink.com.cn')
if mibBuilder.loadTexts: tplinkAclMIB.setDescription('Private MIB for acl.')
tplinkAclMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 11863, 6, 26, 1))
tplinkAclNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 11863, 6, 26, 2))
tpPolicyConfigure = MibIdentifier((1, 3, 6, 1, 4, 1, 11863, 6, 26, 1, 2))
tpPolicyBindConfigure = MibIdentifier((1, 3, 6, 1, 4, 1, 11863, 6, 26, 1, 3))
tpAclBindConfigure = MibIdentifier((1, 3, 6, 1, 4, 1, 11863, 6, 26, 1, 4))
tpPolicyTable = MibTable((1, 3, 6, 1, 4, 1, 11863, 6, 26, 1, 2, 1), )
if mibBuilder.loadTexts: tpPolicyTable.setStatus('current')
if mibBuilder.loadTexts: tpPolicyTable.setDescription('A list of policy entries. Here you can add ACLs and create corresponding actions for the policy.')
tpPolicyEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11863, 6, 26, 1, 2, 1, 1), ).setIndexNames((0, "TPLINK-ACL-MIB", "tpPolicyName"), (0, "TPLINK-ACL-MIB", "tpAclId"))
if mibBuilder.loadTexts: tpPolicyEntry.setStatus('current')
if mibBuilder.loadTexts: tpPolicyEntry.setDescription('An entry contains of the information of policy.')
tpPolicyName = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 26, 1, 2, 1, 1, 1), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tpPolicyName.setStatus('current')
if mibBuilder.loadTexts: tpPolicyName.setDescription('policy name')
tpAclId = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 26, 1, 2, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tpAclId.setStatus('current')
if mibBuilder.loadTexts: tpAclId.setDescription('the aclId must be existent')
tpMirrorPort = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 26, 1, 2, 1, 1, 3), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tpMirrorPort.setStatus('current')
if mibBuilder.loadTexts: tpMirrorPort.setDescription('mirror the data packets in the policy to the specific port. if traffic mirror doesnt work, please set it to 0')
tpConditionRate = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 26, 1, 2, 1, 1, 4), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tpConditionRate.setStatus('current')
if mibBuilder.loadTexts: tpConditionRate.setDescription('limit the transmission rate of the data packets in the policy.(1-1000000Kbps), if traffic condition doesnt work, please set it to 0')
tpIfExceedOperation = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 26, 1, 2, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("none", 0), ("drop", 1)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tpIfExceedOperation.setStatus('current')
if mibBuilder.loadTexts: tpIfExceedOperation.setDescription('Specify the disposal way of the data packets those are transmitted beyond the rate. (you must set the conditionRate firstly)')
tpRedirectPort = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 26, 1, 2, 1, 1, 6), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tpRedirectPort.setStatus('current')
if mibBuilder.loadTexts: tpRedirectPort.setDescription('Forward the data packets those match the corresponding ACL to the specific port, if you want redirect to vlan, please set it to 0')
tpQosRemarkDSCP = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 26, 1, 2, 1, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(64, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63))).clone(namedValues=NamedValues(("dscp64-noLimit", 64), ("dscp0-be-000000", 0), ("dscp1", 1), ("dscp2", 2), ("dscp3", 3), ("dscp4", 4), ("dscp5", 5), ("dscp6", 6), ("dscp7", 7), ("dscp8-cs1-001000", 8), ("dscp9", 9), ("dscp10-af11-001010", 10), ("dscp11", 11), ("dscp12-af12-001100", 12), ("dscp13", 13), ("dscp14-af13-001110", 14), ("dscp15", 15), ("dscp16-cs2-010000", 16), ("dscp17", 17), ("dscp18-af21-010010", 18), ("dscp19", 19), ("dscp20-af22-010100", 20), ("dscp21", 21), ("dscp22-af23-010110", 22), ("dscp23", 23), ("dscp24-cs3-011000", 24), ("dscp25", 25), ("dscp26-af31-011010", 26), ("dscp27", 27), ("dscp28-af32-011100", 28), ("dscp29", 29), ("dscp30-af33-011110", 30), ("dscp31", 31), ("dscp32-cs4-100000", 32), ("dscp33", 33), ("dscp34-af41-100010", 34), ("dscp35", 35), ("dscp36-af42-100100", 36), ("dscp37", 37), ("dscp38-af43-100110", 38), ("dscp39", 39), ("dscp40-cs5-101000", 40), ("dscp41", 41), ("dscp42", 42), ("dscp43", 43), ("dscp44", 44), ("dscp45", 45), ("dscp46-ef-101110", 46), ("dscp47", 47), ("dscp48-cs6-110000", 48), ("dscp49", 49), ("dscp50", 50), ("dscp51", 51), ("dscp52", 52), ("dscp53", 53), ("dscp54", 54), ("dscp55", 55), ("dscp56-cs7-111000", 56), ("dscp57", 57), ("dscp58", 58), ("dscp59", 59), ("dscp60", 60), ("dscp61", 61), ("dscp62", 62), ("dscp63", 63)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tpQosRemarkDSCP.setStatus('current')
if mibBuilder.loadTexts: tpQosRemarkDSCP.setDescription('Specify the DSCP region for the data packets those match the corresponding ACL.')
tpQosRemarkLocalPri = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 26, 1, 2, 1, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8))).clone(namedValues=NamedValues(("default", 0), ("tc0", 1), ("tc1", 2), ("tc2", 3), ("tc3", 4), ("tc4", 5), ("tc5", 6), ("tc6", 7), ("tc7", 8)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tpQosRemarkLocalPri.setStatus('current')
if mibBuilder.loadTexts: tpQosRemarkLocalPri.setDescription('Specify the local priority for the data packets those match the corresponding ACL.')
tpPolicyStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 26, 1, 2, 1, 1, 9), TPRowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tpPolicyStatus.setStatus('current')
if mibBuilder.loadTexts: tpPolicyStatus.setDescription('the following two values are states: these values may be read or written active(1), notInService(2), the following value is a state: this value may be read, but not written notReady(3), the following three values are actions: these values may be written, but are never read createAndGo(4), createAndWait(5), destroy(6)')
tpPolicyBindPortTable = MibTable((1, 3, 6, 1, 4, 1, 11863, 6, 26, 1, 3, 1), )
if mibBuilder.loadTexts: tpPolicyBindPortTable.setStatus('current')
if mibBuilder.loadTexts: tpPolicyBindPortTable.setDescription('A list of policy port binding entries. Here you can bind a policy to a port. ')
tpPolicyBindPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11863, 6, 26, 1, 3, 1, 1), ).setIndexNames((0, "TPLINK-ACL-MIB", "tpBindPortPolicyName"), (0, "TPLINK-ACL-MIB", "tpPolicyPort"))
if mibBuilder.loadTexts: tpPolicyBindPortEntry.setStatus('current')
if mibBuilder.loadTexts: tpPolicyBindPortEntry.setDescription('An entry contains of the information of policy port binding.')
tpBindPortPolicyName = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 26, 1, 3, 1, 1, 1), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tpBindPortPolicyName.setStatus('current')
if mibBuilder.loadTexts: tpBindPortPolicyName.setDescription('The name of the policy you want to bind.(the policy name must be existent)')
tpPolicyPort = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 26, 1, 3, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tpPolicyPort.setStatus('current')
if mibBuilder.loadTexts: tpPolicyPort.setDescription('The port that the policy bind to')
tpPolicyBindPortStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 26, 1, 3, 1, 1, 3), TPRowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tpPolicyBindPortStatus.setStatus('current')
if mibBuilder.loadTexts: tpPolicyBindPortStatus.setDescription('the following two values are states: these values may be read or written active(1), notInService(2), the following value is a state: this value may be read, but not written notReady(3), the following three values are actions: these values may be written, but are never read createAndGo(4), createAndWait(5), destroy(6)')
tpPolicyBindVlanTable = MibTable((1, 3, 6, 1, 4, 1, 11863, 6, 26, 1, 3, 2), )
if mibBuilder.loadTexts: tpPolicyBindVlanTable.setStatus('current')
if mibBuilder.loadTexts: tpPolicyBindVlanTable.setDescription('A list of policy vlan binding entries. Here you can bind a policy to a VLAN.')
tpPolicyBindVlanEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11863, 6, 26, 1, 3, 2, 1), ).setIndexNames((0, "TPLINK-ACL-MIB", "tpBindVlanPolicyName"), (0, "TPLINK-ACL-MIB", "tpPolicyVlan"))
if mibBuilder.loadTexts: tpPolicyBindVlanEntry.setStatus('current')
if mibBuilder.loadTexts: tpPolicyBindVlanEntry.setDescription('An entry contains of the information of policy vlan binding.')
tpBindVlanPolicyName = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 26, 1, 3, 2, 1, 1), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tpBindVlanPolicyName.setStatus('current')
if mibBuilder.loadTexts: tpBindVlanPolicyName.setDescription('The name of the policy you want to bind.(the policy name must be existent)')
tpPolicyVlan = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 26, 1, 3, 2, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tpPolicyVlan.setStatus('current')
if mibBuilder.loadTexts: tpPolicyVlan.setDescription('the vlan that the policy bind to, the vlan must be existent')
tpPolicyBindVlanStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 26, 1, 3, 2, 1, 3), TPRowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tpPolicyBindVlanStatus.setStatus('current')
if mibBuilder.loadTexts: tpPolicyBindVlanStatus.setDescription('the following two values are states: these values may be read or written active(1), notInService(2), the following value is a state: this value may be read, but not written notReady(3), the following three values are actions: these values may be written, but are never read createAndGo(4), createAndWait(5), destroy(6)')
tpAclBindPortTable = MibTable((1, 3, 6, 1, 4, 1, 11863, 6, 26, 1, 4, 1), )
if mibBuilder.loadTexts: tpAclBindPortTable.setStatus('current')
if mibBuilder.loadTexts: tpAclBindPortTable.setDescription('A list of ACL port binding entries. Here you can bind a ACL to a port. ')
tpAclBindPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11863, 6, 26, 1, 4, 1, 1), ).setIndexNames((0, "TPLINK-ACL-MIB", "tpBindPortAclId"), (0, "TPLINK-ACL-MIB", "tpAclPort"))
if mibBuilder.loadTexts: tpAclBindPortEntry.setStatus('current')
if mibBuilder.loadTexts: tpAclBindPortEntry.setDescription('An entry contains of the information of ACL port binding.')
tpBindPortAclId = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 26, 1, 4, 1, 1, 1), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tpBindPortAclId.setStatus('current')
if mibBuilder.loadTexts: tpBindPortAclId.setDescription('The Id of the ACL you want to bind.(the ACL Id must be existent)')
tpAclPort = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 26, 1, 4, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tpAclPort.setStatus('current')
if mibBuilder.loadTexts: tpAclPort.setDescription('The port that the ACL bind to')
tpAclBindPortStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 26, 1, 4, 1, 1, 3), TPRowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tpAclBindPortStatus.setStatus('current')
if mibBuilder.loadTexts: tpAclBindPortStatus.setDescription('the following two values are states: these values may be read or written active(1), notInService(2), the following value is a state: this value may be read, but not written notReady(3), the following three values are actions: these values may be written, but are never read createAndGo(4), createAndWait(5), destroy(6)')
tpAclBindVlanTable = MibTable((1, 3, 6, 1, 4, 1, 11863, 6, 26, 1, 4, 2), )
if mibBuilder.loadTexts: tpAclBindVlanTable.setStatus('current')
if mibBuilder.loadTexts: tpAclBindVlanTable.setDescription('A list of ACL vlan binding entries. Here you can bind a ACL to a VLAN.')
tpAclBindVlanEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11863, 6, 26, 1, 4, 2, 1), ).setIndexNames((0, "TPLINK-ACL-MIB", "tpBindVlanAclId"), (0, "TPLINK-ACL-MIB", "tpAclVlan"))
if mibBuilder.loadTexts: tpAclBindVlanEntry.setStatus('current')
if mibBuilder.loadTexts: tpAclBindVlanEntry.setDescription('An entry contains of the information of ACL vlan binding.')
tpBindVlanAclId = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 26, 1, 4, 2, 1, 1), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tpBindVlanAclId.setStatus('current')
if mibBuilder.loadTexts: tpBindVlanAclId.setDescription('The Id of the ACL you want to bind.(the ACL Id must be existent)')
tpAclVlan = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 26, 1, 4, 2, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tpAclVlan.setStatus('current')
if mibBuilder.loadTexts: tpAclVlan.setDescription('the vlan that the ACL bind to, the vlan must be existent')
tpAclBindVlanStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 26, 1, 4, 2, 1, 3), TPRowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tpAclBindVlanStatus.setStatus('current')
if mibBuilder.loadTexts: tpAclBindVlanStatus.setDescription('the following two values are states: these values may be read or written active(1), notInService(2), the following value is a state: this value may be read, but not written notReady(3), the following three values are actions: these values may be written, but are never read createAndGo(4), createAndWait(5), destroy(6)')
mibBuilder.exportSymbols("TPLINK-ACL-MIB", tpPolicyBindConfigure=tpPolicyBindConfigure, tpAclId=tpAclId, tpMirrorPort=tpMirrorPort, tpAclBindPortTable=tpAclBindPortTable, tpIfExceedOperation=tpIfExceedOperation, tpConditionRate=tpConditionRate, tpPolicyPort=tpPolicyPort, tpQosRemarkLocalPri=tpQosRemarkLocalPri, tpPolicyEntry=tpPolicyEntry, tpPolicyName=tpPolicyName, tpQosRemarkDSCP=tpQosRemarkDSCP, tplinkAclMIBObjects=tplinkAclMIBObjects, tpRedirectPort=tpRedirectPort, tpPolicyBindPortTable=tpPolicyBindPortTable, tpPolicyBindPortEntry=tpPolicyBindPortEntry, tpPolicyBindPortStatus=tpPolicyBindPortStatus, PYSNMP_MODULE_ID=tplinkAclMIB, tpPolicyBindVlanTable=tpPolicyBindVlanTable, tplinkAclMIB=tplinkAclMIB, tpPolicyTable=tpPolicyTable, tpBindVlanAclId=tpBindVlanAclId, tpAclPort=tpAclPort, tpAclBindVlanStatus=tpAclBindVlanStatus, tpBindPortPolicyName=tpBindPortPolicyName, tpAclBindVlanEntry=tpAclBindVlanEntry, tpPolicyBindVlanEntry=tpPolicyBindVlanEntry, tpBindVlanPolicyName=tpBindVlanPolicyName, tpPolicyBindVlanStatus=tpPolicyBindVlanStatus, tpPolicyConfigure=tpPolicyConfigure, tpAclBindPortEntry=tpAclBindPortEntry, tpPolicyVlan=tpPolicyVlan, tpAclBindConfigure=tpAclBindConfigure, tpPolicyStatus=tpPolicyStatus, tpAclBindPortStatus=tpAclBindPortStatus, tplinkAclNotifications=tplinkAclNotifications, tpBindPortAclId=tpBindPortAclId, tpAclBindVlanTable=tpAclBindVlanTable, tpAclVlan=tpAclVlan)
