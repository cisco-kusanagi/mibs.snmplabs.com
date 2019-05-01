#
# PySNMP MIB module CISCO-IETF-PW-FR-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-IETF-PW-FR-MIB
# Produced by pysmi-0.3.4 at Wed May  1 12:00:55 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint")
DlciNumber, = mibBuilder.importSymbols("CISCO-FRAME-RELAY-MIB", "DlciNumber")
CpwVcIndexType, = mibBuilder.importSymbols("CISCO-IETF-PW-TC-MIB", "CpwVcIndexType")
ciscoExperiment, = mibBuilder.importSymbols("CISCO-SMI", "ciscoExperiment")
InterfaceIndexOrZero, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndexOrZero")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
MibIdentifier, TimeTicks, Integer32, ObjectIdentity, Unsigned32, Counter32, NotificationType, ModuleIdentity, IpAddress, Gauge32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "TimeTicks", "Integer32", "ObjectIdentity", "Unsigned32", "Counter32", "NotificationType", "ModuleIdentity", "IpAddress", "Gauge32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "Counter64")
RowStatus, DisplayString, StorageType, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "DisplayString", "StorageType", "TextualConvention")
cpwVcFrMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 10, 112))
cpwVcFrMIB.setRevisions(('2003-12-16 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: cpwVcFrMIB.setRevisionsDescriptions(('Initial version of this MIB module.',))
if mibBuilder.loadTexts: cpwVcFrMIB.setLastUpdated('200312160000Z')
if mibBuilder.loadTexts: cpwVcFrMIB.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: cpwVcFrMIB.setContactInfo('Cisco Systems Customer Service Postal: 170 W. Tasman Drive San Jose, CA 95134 SA Tel: +1 800 553-NETS Email: cs-framerelay@cisco.com')
if mibBuilder.loadTexts: cpwVcFrMIB.setDescription('Cisco Pseudo Wire Frame Relay MIB This MIB describes network management objects defined for FRoPW services over a Packet Switched Network (PSN). As described in the IETF Frame Relay over Pseudowire (FRoPW) draft, draft-ietf-pwe3-frame-relay-01.txt, FR VCs and PW can be mapped in 2 modes: One-to-one mapping mode: a FR VC is mapped to a PW. This mode is described by cpwVcFrTable. Many-to-one mapping mode (a.k.a. port mode): multiple FR VCs assigned to a port are mapped to a PW. This mode is addressed by cpwVcFrPortModeTable. In this mode, all data frames are directed to the associated PSN tunnel regardless of DLCI.')
cpwVcFrNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 112, 0))
cpwVcFrObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 112, 1))
cpwVcFrConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 112, 2))
cpwVcFrTable = MibTable((1, 3, 6, 1, 4, 1, 9, 10, 112, 1, 1), )
if mibBuilder.loadTexts: cpwVcFrTable.setStatus('current')
if mibBuilder.loadTexts: cpwVcFrTable.setDescription("The PW-FR connection table. Each entry in this table represents a FRoPW connection operating in one-to-one mapping mode. This table uses the same index as the generic PW MIB's VC table. Therefore, each entry in cpwVcFrTable has a mapping entry to the generic PW MIB VC table associated by the PW VC index. An entry is created in this table by the agent for every entry in the generic PW MIB VC table with a VcType of 'frameRelay'.")
cpwVcFrEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 10, 112, 1, 1, 1), ).setIndexNames((0, "CISCO-IETF-PW-FR-MIB", "cpwVcFrPwVcIndex"))
if mibBuilder.loadTexts: cpwVcFrEntry.setStatus('current')
if mibBuilder.loadTexts: cpwVcFrEntry.setDescription('An entry in cpwVcFrTable.')
cpwVcFrPwVcIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 112, 1, 1, 1, 1), CpwVcIndexType())
if mibBuilder.loadTexts: cpwVcFrPwVcIndex.setStatus('current')
if mibBuilder.loadTexts: cpwVcFrPwVcIndex.setDescription('This object identifies the index to an entry in the generic PW table.')
cpwVcFrIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 112, 1, 1, 1, 2), InterfaceIndexOrZero()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cpwVcFrIfIndex.setStatus('current')
if mibBuilder.loadTexts: cpwVcFrIfIndex.setDescription('This object identifies the index to an entry in the IF-MIB table. In this case, it holds the ifIndex value of the Frame Relay interface associating with the PW connection. The value of zero means that the InterfaceIndex is not known yet.')
cpwVcFrDlci = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 112, 1, 1, 1, 3), DlciNumber()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cpwVcFrDlci.setStatus('current')
if mibBuilder.loadTexts: cpwVcFrDlci.setDescription('This object identifies the FR DLCI associating with this entry in cpwVcFrTable. This object can be used together with cpwVcFrIfIndex to lookup FR VC specific information for the FR PVC segment of a FRoPW connection.')
cpwVcFrAdminStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 112, 1, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("up", 1), ("down", 2)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cpwVcFrAdminStatus.setStatus('current')
if mibBuilder.loadTexts: cpwVcFrAdminStatus.setDescription("This value of this object indicates the administrative status of the FRoPW connection. The values mean: up(1) - connection is administratively set to the 'up' state for handling traffic. down(2) - connection is administratively set to the 'down' state. No traffic is processed at this state.")
cpwVcFrOperStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 112, 1, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("active", 1), ("inactive", 2), ("unknown", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpwVcFrOperStatus.setStatus('current')
if mibBuilder.loadTexts: cpwVcFrOperStatus.setDescription('This is actual operational status of the logical FRoPW connection, which is derived from combining the following 2 operational status: cpwVcFrPw2FrOperStatus Operational status of the FR segment on the FRoPW connection. PW Operation Status Operational status of the PW segment of the FRoPW connection. The associated object is cpwVcOperStatus from the generic PW MIB.')
cpwVcFrPw2FrOperStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 112, 1, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("active", 1), ("inactive", 2), ("unknown", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpwVcFrPw2FrOperStatus.setStatus('current')
if mibBuilder.loadTexts: cpwVcFrPw2FrOperStatus.setDescription('The value of the object identifies the current operational status of the FR PVC segment of a FRoPW connection. The values mean: active(1) - segment is currently operational. inactive(2) - segment in currently not operational. unknown(3) - segment current status cannot be determined.')
cpwVcFrRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 112, 1, 1, 1, 7), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cpwVcFrRowStatus.setStatus('current')
if mibBuilder.loadTexts: cpwVcFrRowStatus.setDescription('For creating, modifying, and deleting this row.')
cpwVcFrStorageType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 112, 1, 1, 1, 8), StorageType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cpwVcFrStorageType.setStatus('current')
if mibBuilder.loadTexts: cpwVcFrStorageType.setDescription('Indicates the storage type of this row.')
cpwVcFrPMTable = MibTable((1, 3, 6, 1, 4, 1, 9, 10, 112, 1, 2), )
if mibBuilder.loadTexts: cpwVcFrPMTable.setStatus('current')
if mibBuilder.loadTexts: cpwVcFrPMTable.setDescription("The PW-FR port mode connection table. Each entry in this table represents a FRoPW connection operating in the port mode. This table uses the same index as the generic PW MIB's VC table. Therefore, each entry in cpwVcFrTable has a mapping entry to the generic PW MIB VC table associated by the PW VC index. An entry is created in this table by the agent for every entry in the generic PW MIB VC table with a VcType of 'frameRelayPortMode'.")
cpwVcFrPMEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 10, 112, 1, 2, 1), ).setIndexNames((0, "CISCO-IETF-PW-FR-MIB", "cpwVcFrPMPwVcIndex"))
if mibBuilder.loadTexts: cpwVcFrPMEntry.setStatus('current')
if mibBuilder.loadTexts: cpwVcFrPMEntry.setDescription('An entry in cpwVcFrPMTable.')
cpwVcFrPMPwVcIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 112, 1, 2, 1, 1), CpwVcIndexType())
if mibBuilder.loadTexts: cpwVcFrPMPwVcIndex.setStatus('current')
if mibBuilder.loadTexts: cpwVcFrPMPwVcIndex.setDescription('This object identifies the index to an entry in the generic PW table.')
cpwVcFrPMIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 112, 1, 2, 1, 2), InterfaceIndexOrZero()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cpwVcFrPMIfIndex.setStatus('current')
if mibBuilder.loadTexts: cpwVcFrPMIfIndex.setDescription('This object represents the FR port associating with the FRoPW connection operating in port mode. The value in the index identifies an entry in the IF-MIB table. The value of zero means that the InterfaceIndex is not known yet.')
cpwVcFrPMAdminStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 112, 1, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("up", 1), ("down", 2)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cpwVcFrPMAdminStatus.setStatus('current')
if mibBuilder.loadTexts: cpwVcFrPMAdminStatus.setDescription("This value of this object indicates the administrative status of the FRoPW connection. The values mean: up(1) - connection is administratively set to the 'up' state for handling traffic. down(2) - connection is administratively set to the 'down' state. No traffic is processed at this state.")
cpwVcFrPMOperStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 112, 1, 2, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("active", 1), ("inactive", 2), ("unknown", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpwVcFrPMOperStatus.setStatus('current')
if mibBuilder.loadTexts: cpwVcFrPMOperStatus.setDescription('This is actual operational status of the logical FRoPW connection in port mode, which is derived from combining the following 2 operational status: cpwVcFrPMPw2FrOperStatus Operational status of the FR segment on the FRoPW connection. PW Operation Status Operational status of the PW segment of the FRoPW connection. The associated object is cpwVcOperStatus from the generic PW MIB.')
cpwVcFrPMPw2FrOperStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 112, 1, 2, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("active", 1), ("inactive", 2), ("unknown", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpwVcFrPMPw2FrOperStatus.setStatus('current')
if mibBuilder.loadTexts: cpwVcFrPMPw2FrOperStatus.setDescription('The value of the object identifies the current operational status of the associate FR port. The values mean: active(1) - segment is currently operational. inactive(2) - segment in currently not operational. unknown(3) - segment current status cannot be determined.')
cpwVcFrPMRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 112, 1, 2, 1, 6), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cpwVcFrPMRowStatus.setStatus('current')
if mibBuilder.loadTexts: cpwVcFrPMRowStatus.setDescription('For creating, modifying, and deleting this row.')
cpwVcFrPMStorageType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 112, 1, 2, 1, 7), StorageType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cpwVcFrPMStorageType.setStatus('current')
if mibBuilder.loadTexts: cpwVcFrPMStorageType.setDescription('Indicates the storage type of this row.')
cpwVcFrCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 112, 2, 1))
cpwVcFrGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 112, 2, 2))
cpwVcFrFullCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 10, 112, 2, 1, 1)).setObjects(("CISCO-IETF-PW-FR-MIB", "cpwVcFrGroup"), ("CISCO-IETF-PW-FR-MIB", "cpwVcFrPMGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cpwVcFrFullCompliance = cpwVcFrFullCompliance.setStatus('current')
if mibBuilder.loadTexts: cpwVcFrFullCompliance.setDescription('The compliance statement for agents that provide full support for the PW-FR-MIB module.')
cpwVcFrReadOnlyCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 10, 112, 2, 1, 2)).setObjects(("CISCO-IETF-PW-FR-MIB", "cpwVcFrGroup"), ("CISCO-IETF-PW-FR-MIB", "cpwVcFrPMGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cpwVcFrReadOnlyCompliance = cpwVcFrReadOnlyCompliance.setStatus('current')
if mibBuilder.loadTexts: cpwVcFrReadOnlyCompliance.setDescription('The compliance statement for agents that only provide read-only support for the PW-FR-MIB module.')
cpwVcFrGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 10, 112, 2, 2, 1)).setObjects(("CISCO-IETF-PW-FR-MIB", "cpwVcFrIfIndex"), ("CISCO-IETF-PW-FR-MIB", "cpwVcFrDlci"), ("CISCO-IETF-PW-FR-MIB", "cpwVcFrAdminStatus"), ("CISCO-IETF-PW-FR-MIB", "cpwVcFrOperStatus"), ("CISCO-IETF-PW-FR-MIB", "cpwVcFrPw2FrOperStatus"), ("CISCO-IETF-PW-FR-MIB", "cpwVcFrRowStatus"), ("CISCO-IETF-PW-FR-MIB", "cpwVcFrStorageType"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cpwVcFrGroup = cpwVcFrGroup.setStatus('current')
if mibBuilder.loadTexts: cpwVcFrGroup.setDescription('Objects to support cpwVcFrTable.')
cpwVcFrPMGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 10, 112, 2, 2, 2)).setObjects(("CISCO-IETF-PW-FR-MIB", "cpwVcFrPMIfIndex"), ("CISCO-IETF-PW-FR-MIB", "cpwVcFrPMAdminStatus"), ("CISCO-IETF-PW-FR-MIB", "cpwVcFrPMOperStatus"), ("CISCO-IETF-PW-FR-MIB", "cpwVcFrPMPw2FrOperStatus"), ("CISCO-IETF-PW-FR-MIB", "cpwVcFrPMRowStatus"), ("CISCO-IETF-PW-FR-MIB", "cpwVcFrPMStorageType"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cpwVcFrPMGroup = cpwVcFrPMGroup.setStatus('current')
if mibBuilder.loadTexts: cpwVcFrPMGroup.setDescription('Objects to support cpwVcFrPMTable.')
mibBuilder.exportSymbols("CISCO-IETF-PW-FR-MIB", cpwVcFrPw2FrOperStatus=cpwVcFrPw2FrOperStatus, cpwVcFrGroups=cpwVcFrGroups, cpwVcFrPMPwVcIndex=cpwVcFrPMPwVcIndex, cpwVcFrPMEntry=cpwVcFrPMEntry, cpwVcFrGroup=cpwVcFrGroup, cpwVcFrStorageType=cpwVcFrStorageType, PYSNMP_MODULE_ID=cpwVcFrMIB, cpwVcFrDlci=cpwVcFrDlci, cpwVcFrPMStorageType=cpwVcFrPMStorageType, cpwVcFrPMGroup=cpwVcFrPMGroup, cpwVcFrObjects=cpwVcFrObjects, cpwVcFrCompliances=cpwVcFrCompliances, cpwVcFrIfIndex=cpwVcFrIfIndex, cpwVcFrConformance=cpwVcFrConformance, cpwVcFrPMTable=cpwVcFrPMTable, cpwVcFrPMAdminStatus=cpwVcFrPMAdminStatus, cpwVcFrPMRowStatus=cpwVcFrPMRowStatus, cpwVcFrEntry=cpwVcFrEntry, cpwVcFrPMPw2FrOperStatus=cpwVcFrPMPw2FrOperStatus, cpwVcFrNotifications=cpwVcFrNotifications, cpwVcFrPMOperStatus=cpwVcFrPMOperStatus, cpwVcFrPMIfIndex=cpwVcFrPMIfIndex, cpwVcFrMIB=cpwVcFrMIB, cpwVcFrReadOnlyCompliance=cpwVcFrReadOnlyCompliance, cpwVcFrTable=cpwVcFrTable, cpwVcFrPwVcIndex=cpwVcFrPwVcIndex, cpwVcFrAdminStatus=cpwVcFrAdminStatus, cpwVcFrRowStatus=cpwVcFrRowStatus, cpwVcFrFullCompliance=cpwVcFrFullCompliance, cpwVcFrOperStatus=cpwVcFrOperStatus)