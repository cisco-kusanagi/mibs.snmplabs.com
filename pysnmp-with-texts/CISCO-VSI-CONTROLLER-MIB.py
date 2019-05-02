#
# PySNMP MIB module CISCO-VSI-CONTROLLER-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-VSI-CONTROLLER-MIB
# Produced by pysmi-0.3.4 at Wed May  1 12:19:49 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
TimeTicks, ModuleIdentity, Counter64, Unsigned32, iso, IpAddress, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, Counter32, MibIdentifier, NotificationType, Integer32, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "ModuleIdentity", "Counter64", "Unsigned32", "iso", "IpAddress", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "Counter32", "MibIdentifier", "NotificationType", "Integer32", "Gauge32")
RowStatus, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "DisplayString", "TextualConvention")
ciscoVSIControllerMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 141))
if mibBuilder.loadTexts: ciscoVSIControllerMIB.setLastUpdated('9906080000Z')
if mibBuilder.loadTexts: ciscoVSIControllerMIB.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoVSIControllerMIB.setContactInfo('Cisco Systems Customer Service Postal: 170 W Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-wanatm@cisco.com')
if mibBuilder.loadTexts: ciscoVSIControllerMIB.setDescription("This MIB module is used for configuring ATM Capable Switch to be aware of VSI Controller information. Terminolgies used: VSI - Virtual Switch Interface, a hardware-independent switch control protocol. This allows a Switch(node) to be controlled by a multiple controllers such as PNNI,LSC. These control planes can be internal or external to the switch.The VSI interface defines the messages and associated functions which allow communication between the controller and the switch.This interface is expected to support all types of connections (voice,data,frame relay,ATM) for PVCs, SPVCs and SVCs. VSI Master - software component which requests connections and receives switch generic information. This controls one or more VSI Slaves. This may run on the switch or a dedicated controller platform. This is the master module.It performs the interface to the higher layer networking software and handles all VSI related functions. VSI Slave - software component which converts generic connection requests into hardware specific requests and hardware specific information into generic information. This runs on the switch.a A centralized slave has a single point of control for making connections and controlling interfaces, while a distributed slave allows for multiple slaves to coexist on the same switch. Controller - Software ( and possibly hardware) which manages topology and network resources and performs VSI Master fucntion. This performs source routing for ent-to-end SVCs, including general call acceptance GCAC,setup calls with other controllers. PNNI and MPLS are examples for the Controller. Controller Shelf - A controller shelf is a switch containing atleast one VSI Controller which is controlling a different switch.It will also, typically, contain 'local' controllers for itself.")
class CvcControllerShelfLocation(TextualConvention, Integer32):
    description = 'The location of the Controller Shelf. internal(1) - controller resides on the same shelf as the switch. external(2) - controller resides on the external platform. The controller shelf is connected to the switch by an ATM link.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("internal", 1), ("external", 2))

class CvcControllerType(TextualConvention, Integer32):
    description = "The type of the controller which is a VSI Master. The Possible values are : par(1) - Portable Auto Route(PAR). This is a VSI Master controller implementing Cisco Proprietary protocol for network routing and topology in a Network containing only Cisco Switches. pnni(2) - Private Network-to-Network Interface (PNNI) controller. The PNNI protocol is used between private ATM Switches and between groups of ATM switches. This protocol is defined for distributing topology information between switches and clusters of switches. lsc(3) - Label Switch Controller(TSC).The LSC Implements MPLS (Multi Protocol Label Switching) protocol. The LSC is a router which is capable of controlling the operation of a separate ATM switch so that the two of them together function as a single ATM-LSR(ATM Label Switch Router). The LSC controls the operation of the ATM Switch using a 'Switch Control Protocol', which allows the LSC to setup and remove cross-connects on the ATM switch, to discover the configuration and capabilities of the controlled switch, and to gather statistics from the controlled switch."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("par", 1), ("pnni", 2), ("lsc", 3))

cvcMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 141, 1))
cvcConfController = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 141, 1, 1))
cvcConfTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 141, 1, 1, 1), )
if mibBuilder.loadTexts: cvcConfTable.setStatus('current')
if mibBuilder.loadTexts: cvcConfTable.setDescription('This table contains the entries for VSI Controllers. This table is used for informing the VSI Slaves about the existence of VSI Controllers and how the VSI slaves can reach the controller. The information in these entries are advertised to all the VSI Slaves using a system dependent implementation when an entry is created/activated.')
cvcConfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 141, 1, 1, 1, 1), ).setIndexNames((0, "CISCO-VSI-CONTROLLER-MIB", "cvcConfControllerID"))
if mibBuilder.loadTexts: cvcConfEntry.setStatus('current')
if mibBuilder.loadTexts: cvcConfEntry.setDescription("An entry for a VSI Controller. The entries in this table are created by setting the cvcConfRowStatus object to 'createAndGo(4)'. The entries in this table are deleted by setting the cvcConfRowStatus object to 'destroy(6)'. The entries are can be created/modified/deleted through the Command Line Interface(CLI) also.")
cvcConfControllerID = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 141, 1, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: cvcConfControllerID.setStatus('current')
if mibBuilder.loadTexts: cvcConfControllerID.setDescription('This is the unique value for VSI Controller(VSI Master). The VSI Slave uses this value in the message to identify the VSI Master controller.')
cvcConfControllerType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 141, 1, 1, 1, 1, 2), CvcControllerType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cvcConfControllerType.setStatus('current')
if mibBuilder.loadTexts: cvcConfControllerType.setDescription("This object identifies the controller type. This object may not be modified if the associated cvcConfRowStatus is equal to 'active(1)'.")
cvcConfControllerShelfLocation = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 141, 1, 1, 1, 1, 3), CvcControllerShelfLocation()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cvcConfControllerShelfLocation.setStatus('current')
if mibBuilder.loadTexts: cvcConfControllerShelfLocation.setDescription('This identifies the location of the controller shelf. This Object can be set only during row creation.')
cvcConfControllerLocation = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 141, 1, 1, 1, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cvcConfControllerLocation.setStatus('current')
if mibBuilder.loadTexts: cvcConfControllerLocation.setDescription("This identifies the location of the controller. This object might contain the logical slot number of the Module where the controller is running on the same shelf as the switch. This object might contain the value of the interface on the module where the controller is running on an external shelf connected to the switch. This object may not be modified if the associated cvcConfRowStatus is equal to 'active(1)'.")
cvcConfControllerName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 141, 1, 1, 1, 1, 5), DisplayString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cvcConfControllerName.setStatus('current')
if mibBuilder.loadTexts: cvcConfControllerName.setDescription("This is the name choosen by the user for the VSI Controller. This object contains Octet string of length zero, if the user does not set the value for this object. This object may not be modified if the associated cvcConfRowStatus is equal to 'active(1)'.")
cvcConfVpi = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 141, 1, 1, 1, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 4095))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cvcConfVpi.setStatus('current')
if mibBuilder.loadTexts: cvcConfVpi.setDescription("This is the Virtual Path Identifier(VPI) used for connecting to the controller which is external to the switch. This object has significance only if cvcConfControllerShelfLocation is 'external(2)'. This object may not be modified if the associated cvcConfRowStatus is equal to 'active(1)'.")
cvcConfVci = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 141, 1, 1, 1, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(32, 65535))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cvcConfVci.setStatus('current')
if mibBuilder.loadTexts: cvcConfVci.setDescription("This is the start value of Virtual Channel Identifier(VCI) used for connecting to the controller which is external to the switch. This object has significance only if cvcConfControllerShelfLocation is 'external(2)'. This object may not be modified if the associated cvcConfRowStatus is equal to 'active(1)'.")
cvcConfRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 141, 1, 1, 1, 1, 8), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cvcConfRowStatus.setStatus('current')
if mibBuilder.loadTexts: cvcConfRowStatus.setDescription("This object is used for adding,deleting and modifying the controller configuration. The row can be created by setting this object to 'createAndGo(4)'. The row can be deleted by setting this object to 'destroy(6)'. The objects in the row can not be modified when this object contains value 'active(1)'.")
cvcMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 141, 3))
cvcMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 141, 3, 1))
cvcMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 141, 3, 2))
cvcMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 141, 3, 1, 1)).setObjects(("CISCO-VSI-CONTROLLER-MIB", "cvcConfGroup"), ("CISCO-VSI-CONTROLLER-MIB", "cvcConfGroupExternal"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cvcMIBCompliance = cvcMIBCompliance.setStatus('current')
if mibBuilder.loadTexts: cvcMIBCompliance.setDescription('The Compliance statement for cisco VSI Controller group.')
cvcConfGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 141, 3, 2, 1)).setObjects(("CISCO-VSI-CONTROLLER-MIB", "cvcConfControllerType"), ("CISCO-VSI-CONTROLLER-MIB", "cvcConfControllerShelfLocation"), ("CISCO-VSI-CONTROLLER-MIB", "cvcConfControllerLocation"), ("CISCO-VSI-CONTROLLER-MIB", "cvcConfControllerName"), ("CISCO-VSI-CONTROLLER-MIB", "cvcConfRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cvcConfGroup = cvcConfGroup.setStatus('current')
if mibBuilder.loadTexts: cvcConfGroup.setDescription('The objects related to configuring VSI controllers running on the same shelf as the switch. ')
cvcConfGroupExternal = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 141, 3, 2, 2)).setObjects(("CISCO-VSI-CONTROLLER-MIB", "cvcConfVpi"), ("CISCO-VSI-CONTROLLER-MIB", "cvcConfVci"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cvcConfGroupExternal = cvcConfGroupExternal.setStatus('current')
if mibBuilder.loadTexts: cvcConfGroupExternal.setDescription('The objects related to configuring VSI controllers running on the shelf external to the switch. ')
mibBuilder.exportSymbols("CISCO-VSI-CONTROLLER-MIB", CvcControllerShelfLocation=CvcControllerShelfLocation, cvcConfControllerShelfLocation=cvcConfControllerShelfLocation, cvcConfControllerType=cvcConfControllerType, ciscoVSIControllerMIB=ciscoVSIControllerMIB, cvcConfControllerID=cvcConfControllerID, cvcConfVci=cvcConfVci, cvcMIBCompliances=cvcMIBCompliances, cvcConfRowStatus=cvcConfRowStatus, cvcMIBObjects=cvcMIBObjects, cvcMIBCompliance=cvcMIBCompliance, cvcConfVpi=cvcConfVpi, cvcConfEntry=cvcConfEntry, cvcConfGroupExternal=cvcConfGroupExternal, cvcMIBGroups=cvcMIBGroups, cvcConfControllerLocation=cvcConfControllerLocation, cvcConfGroup=cvcConfGroup, cvcConfController=cvcConfController, CvcControllerType=CvcControllerType, cvcMIBConformance=cvcMIBConformance, PYSNMP_MODULE_ID=ciscoVSIControllerMIB, cvcConfControllerName=cvcConfControllerName, cvcConfTable=cvcConfTable)
