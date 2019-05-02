#
# PySNMP MIB module HPN-ICF-EPON-FB-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HPN-ICF-EPON-FB-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:38:34 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint")
hpnicfEpon, = mibBuilder.importSymbols("HPN-ICF-OID-MIB", "hpnicfEpon")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
ModuleIdentity, Counter64, TimeTicks, ObjectIdentity, Unsigned32, IpAddress, Counter32, NotificationType, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, Integer32, MibIdentifier, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "TimeTicks", "ObjectIdentity", "Unsigned32", "IpAddress", "Counter32", "NotificationType", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "Integer32", "MibIdentifier", "Bits")
RowStatus, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "TextualConvention", "DisplayString")
hpnicfEponFBMibObjects = ModuleIdentity((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 6))
if mibBuilder.loadTexts: hpnicfEponFBMibObjects.setLastUpdated('200711271008Z')
if mibBuilder.loadTexts: hpnicfEponFBMibObjects.setOrganization('')
if mibBuilder.loadTexts: hpnicfEponFBMibObjects.setContactInfo('')
if mibBuilder.loadTexts: hpnicfEponFBMibObjects.setDescription(' The objects in this MIB module are used to manage and display current configuration of fiber backup groups based on EPON OLT port. ')
hpnicfEponFBMIB = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 6, 1))
hpnicfEponFBMIBTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 6, 1, 1), )
if mibBuilder.loadTexts: hpnicfEponFBMIBTable.setStatus('current')
if mibBuilder.loadTexts: hpnicfEponFBMIBTable.setDescription('This table defines several optical fiber-backup system parameters.')
hpnicfEponFBMIBEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 6, 1, 1, 1), ).setIndexNames((0, "HPN-ICF-EPON-FB-MIB", "hpnicfEponFBGroupIndex"))
if mibBuilder.loadTexts: hpnicfEponFBMIBEntry.setStatus('current')
if mibBuilder.loadTexts: hpnicfEponFBMIBEntry.setDescription('The entry of hpnicfEponFBMIBTable.')
hpnicfEponFBGroupIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 6, 1, 1, 1, 1), Integer32())
if mibBuilder.loadTexts: hpnicfEponFBGroupIndex.setStatus('current')
if mibBuilder.loadTexts: hpnicfEponFBGroupIndex.setDescription('The EPON fiber-backup group ID.')
hpnicfEponFBGroupRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 6, 1, 1, 1, 2), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpnicfEponFBGroupRowStatus.setStatus('current')
if mibBuilder.loadTexts: hpnicfEponFBGroupRowStatus.setDescription('This object allows entry to be created and deleted from the hpnicfEponFBMIBTable.')
hpnicfEponFBMasterPort = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 6, 1, 1, 1, 3), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpnicfEponFBMasterPort.setStatus('current')
if mibBuilder.loadTexts: hpnicfEponFBMasterPort.setDescription('OLT port ifindex of the fiber-backup group. Use it to set or get the group master port.')
hpnicfEponFBSlavePort = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 6, 1, 1, 1, 4), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpnicfEponFBSlavePort.setStatus('current')
if mibBuilder.loadTexts: hpnicfEponFBSlavePort.setDescription('OLT port ifindex of the fiber-backup group. Use it to set or get the group slave port. hpnicfEponFBSlavePort must be set after hpnicfEponFBMasterPort. ')
hpnicfEponFBMasterPortStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 6, 1, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("active", 1), ("down", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfEponFBMasterPortStatus.setStatus('current')
if mibBuilder.loadTexts: hpnicfEponFBMasterPortStatus.setDescription("The master port status of the fiber-backup group. The active state indicates that the port's role is master, the olt chip is right and the optical module is inserted. The down state indicates others conditions.")
hpnicfEponFBSlavePortStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 6, 1, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("ready", 1), ("down", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfEponFBSlavePortStatus.setStatus('current')
if mibBuilder.loadTexts: hpnicfEponFBSlavePortStatus.setDescription("The slave port status of the fiber-backup group. The ready state indicates that the port's role is slave, the olt chip is right and optical module is inserted. The down state indicates others conditions.")
hpnicfEponFBSwitchover = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 6, 1, 1, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("false", 1), ("true", 2)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpnicfEponFBSwitchover.setStatus('current')
if mibBuilder.loadTexts: hpnicfEponFBSwitchover.setDescription("Switch the fiber backup group's two port manually. The group must has two ports and the value of hpnicfEponFBSlavePortStatus must be ready before Switchover. after Switchover the port's role will be changed. The value true is for switch-over. The default value is false.")
mibBuilder.exportSymbols("HPN-ICF-EPON-FB-MIB", hpnicfEponFBMIBTable=hpnicfEponFBMIBTable, PYSNMP_MODULE_ID=hpnicfEponFBMibObjects, hpnicfEponFBSlavePortStatus=hpnicfEponFBSlavePortStatus, hpnicfEponFBSwitchover=hpnicfEponFBSwitchover, hpnicfEponFBMasterPortStatus=hpnicfEponFBMasterPortStatus, hpnicfEponFBMIBEntry=hpnicfEponFBMIBEntry, hpnicfEponFBMibObjects=hpnicfEponFBMibObjects, hpnicfEponFBSlavePort=hpnicfEponFBSlavePort, hpnicfEponFBGroupRowStatus=hpnicfEponFBGroupRowStatus, hpnicfEponFBGroupIndex=hpnicfEponFBGroupIndex, hpnicfEponFBMIB=hpnicfEponFBMIB, hpnicfEponFBMasterPort=hpnicfEponFBMasterPort)
