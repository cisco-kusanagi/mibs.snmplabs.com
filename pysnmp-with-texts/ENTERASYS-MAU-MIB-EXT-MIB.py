#
# PySNMP MIB module ENTERASYS-MAU-MIB-EXT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ENTERASYS-MAU-MIB-EXT-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:03:55 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint")
etsysModules, = mibBuilder.importSymbols("ENTERASYS-MIB-NAMES", "etsysModules")
ifMauIfIndex, = mibBuilder.importSymbols("MAU-MIB", "ifMauIfIndex")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
Counter32, iso, NotificationType, TimeTicks, IpAddress, Bits, Counter64, Gauge32, Unsigned32, MibIdentifier, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "iso", "NotificationType", "TimeTicks", "IpAddress", "Bits", "Counter64", "Gauge32", "Unsigned32", "MibIdentifier", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "ObjectIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
etsysMauMibExtMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 5624, 1, 2, 59))
etsysMauMibExtMIB.setRevisions(('2006-05-09 11:30', '2006-02-16 19:18', '2005-02-07 15:05',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: etsysMauMibExtMIB.setRevisionsDescriptions(('Deprecated etsysIfMauExtMasterSlaveTable, etsysMauMibExtMasterSlaveGroup, and etsysMauMibExtMasterSlaveCompliance.', 'Added etsysIfMauExtMasterSlaveTable to allow the manual configuration of the master/slave of the MAU.', 'The initial version of this MIB module.',))
if mibBuilder.loadTexts: etsysMauMibExtMIB.setLastUpdated('200605091130Z')
if mibBuilder.loadTexts: etsysMauMibExtMIB.setOrganization('Enterasys Networks, Inc.')
if mibBuilder.loadTexts: etsysMauMibExtMIB.setContactInfo('Postal: Enterasys Networks 50 Minuteman Rd. Andover, MA 01810-1008 USA Phone: +1 978 684 1000 E-mail: support@enterasys.com WWW: http://www.enterasys.com')
if mibBuilder.loadTexts: etsysMauMibExtMIB.setDescription('This MIB module defines a portion of the SNMP MIB under the Enterasys Networks enterprise OID that provide extensions to the industry standard MAU-MIB.')
etsysMauMibExtObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 59, 1))
etsysMauMibExtBasic = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 59, 1, 1))
etsysIfMauExtMDIXTable = MibTable((1, 3, 6, 1, 4, 1, 5624, 1, 2, 59, 1, 1, 1), )
if mibBuilder.loadTexts: etsysIfMauExtMDIXTable.setStatus('current')
if mibBuilder.loadTexts: etsysIfMauExtMDIXTable.setDescription('A table of management information used to control the MDI crossover and extend the base ifMauTable defined in RFC3636.')
etsysIfMauExtMDIXEntry = MibTableRow((1, 3, 6, 1, 4, 1, 5624, 1, 2, 59, 1, 1, 1, 1), ).setIndexNames((0, "MAU-MIB", "ifMauIfIndex"))
if mibBuilder.loadTexts: etsysIfMauExtMDIXEntry.setReference("RFC 3636, 'Definitions of Managed Objects for IEEE 802.3 Medium Attachment Units (MAUs)'")
if mibBuilder.loadTexts: etsysIfMauExtMDIXEntry.setStatus('current')
if mibBuilder.loadTexts: etsysIfMauExtMDIXEntry.setDescription('An entry in the table containing MDI crossover management information per MAU interface.')
etsysIfMauExtMDIXStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 59, 1, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("auto", 1), ("mdix", 2), ("mdi", 3))).clone('auto')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: etsysIfMauExtMDIXStatus.setStatus('current')
if mibBuilder.loadTexts: etsysIfMauExtMDIXStatus.setDescription('The value of this object determines the MDI crossover state of the port. A value of auto(1) enables the port to automatically detect and activate the appropriate rx/tx crossover configuration. A value of mdix(2) will force the port to operate as a MDIX port, which is the standard wiring configuration for a switch port. A value of mdi(3) will force the port to operate as a MDI port, with no internal rx/tx crossover. This object is independent of and not affected by auto-negotiation setting.')
etsysIfMauExtMasterSlaveTable = MibTable((1, 3, 6, 1, 4, 1, 5624, 1, 2, 59, 1, 1, 2), )
if mibBuilder.loadTexts: etsysIfMauExtMasterSlaveTable.setStatus('deprecated')
if mibBuilder.loadTexts: etsysIfMauExtMasterSlaveTable.setDescription('********* THIS TABLE IS DEPRECATED ********** A table of management information used to control the master/slave configuration and extend the base ifMauTable defined in RFC3636.')
etsysIfMauExtMasterSlaveEntry = MibTableRow((1, 3, 6, 1, 4, 1, 5624, 1, 2, 59, 1, 1, 2, 1), ).setIndexNames((0, "MAU-MIB", "ifMauIfIndex"))
if mibBuilder.loadTexts: etsysIfMauExtMasterSlaveEntry.setReference("RFC 3636, 'Definitions of Managed Objects for IEEE 802.3 Medium Attachment Units (MAUs)'")
if mibBuilder.loadTexts: etsysIfMauExtMasterSlaveEntry.setStatus('deprecated')
if mibBuilder.loadTexts: etsysIfMauExtMasterSlaveEntry.setDescription('An entry in the table containing master/slave management information per MAU interface.')
etsysIfMauExtMasterSlaveStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 59, 1, 1, 2, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("master", 1), ("slave", 2))).clone('slave')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: etsysIfMauExtMasterSlaveStatus.setStatus('deprecated')
if mibBuilder.loadTexts: etsysIfMauExtMasterSlaveStatus.setDescription('If auto-negotiation is not enabled, the value of this object determines the master/slave state for this MAU. A value of master(1) will force the port to operate as a master. A value of slave(2) will force the port to operate as a slave.')
etsysMauMibExtConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 59, 2))
etsysMauMibExtGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 59, 2, 1))
etsysMauMibExtCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 59, 2, 2))
etsysMauMibExtMDIXGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 5624, 1, 2, 59, 2, 1, 1)).setObjects(("ENTERASYS-MAU-MIB-EXT-MIB", "etsysIfMauExtMDIXStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    etsysMauMibExtMDIXGroup = etsysMauMibExtMDIXGroup.setStatus('current')
if mibBuilder.loadTexts: etsysMauMibExtMDIXGroup.setDescription('The group that controls the MDI transmit and receive pairs crossover for a given MAU interface.')
etsysMauMibExtMasterSlaveGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 5624, 1, 2, 59, 2, 1, 2)).setObjects(("ENTERASYS-MAU-MIB-EXT-MIB", "etsysIfMauExtMasterSlaveStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    etsysMauMibExtMasterSlaveGroup = etsysMauMibExtMasterSlaveGroup.setStatus('deprecated')
if mibBuilder.loadTexts: etsysMauMibExtMasterSlaveGroup.setDescription('******** THIS CONFORMANCE IS DEPRECATED ******** The group that controls the master/slave configuration for a given MAU interface.')
etsysMauMibExtMDIXCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 5624, 1, 2, 59, 2, 2, 1)).setObjects(("ENTERASYS-MAU-MIB-EXT-MIB", "etsysMauMibExtMDIXGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    etsysMauMibExtMDIXCompliance = etsysMauMibExtMDIXCompliance.setStatus('current')
if mibBuilder.loadTexts: etsysMauMibExtMDIXCompliance.setDescription('The compliance statement for devices that support the MDI crossover functionality for MAU interfaces.')
etsysMauMibExtMasterSlaveCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 5624, 1, 2, 59, 2, 2, 2)).setObjects(("ENTERASYS-MAU-MIB-EXT-MIB", "etsysMauMibExtMasterSlaveGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    etsysMauMibExtMasterSlaveCompliance = etsysMauMibExtMasterSlaveCompliance.setStatus('deprecated')
if mibBuilder.loadTexts: etsysMauMibExtMasterSlaveCompliance.setDescription('******** THIS COMPLIANCE IS DEPRECATED ******** The compliance statement for devices that support the master/slave configuration functionality for MAU interfaces.')
mibBuilder.exportSymbols("ENTERASYS-MAU-MIB-EXT-MIB", etsysMauMibExtObjects=etsysMauMibExtObjects, etsysMauMibExtMDIXCompliance=etsysMauMibExtMDIXCompliance, etsysMauMibExtGroups=etsysMauMibExtGroups, etsysMauMibExtMasterSlaveCompliance=etsysMauMibExtMasterSlaveCompliance, etsysMauMibExtBasic=etsysMauMibExtBasic, etsysIfMauExtMasterSlaveStatus=etsysIfMauExtMasterSlaveStatus, etsysMauMibExtMasterSlaveGroup=etsysMauMibExtMasterSlaveGroup, PYSNMP_MODULE_ID=etsysMauMibExtMIB, etsysMauMibExtCompliances=etsysMauMibExtCompliances, etsysIfMauExtMasterSlaveEntry=etsysIfMauExtMasterSlaveEntry, etsysIfMauExtMDIXTable=etsysIfMauExtMDIXTable, etsysMauMibExtMIB=etsysMauMibExtMIB, etsysIfMauExtMasterSlaveTable=etsysIfMauExtMasterSlaveTable, etsysMauMibExtMDIXGroup=etsysMauMibExtMDIXGroup, etsysIfMauExtMDIXStatus=etsysIfMauExtMDIXStatus, etsysMauMibExtConformance=etsysMauMibExtConformance, etsysIfMauExtMDIXEntry=etsysIfMauExtMDIXEntry)
