#
# PySNMP MIB module AT-IP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/AT-IP-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:30:15 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection")
modules, = mibBuilder.importSymbols("AT-SMI-MIB", "modules")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
InetAddressType, InetAddress = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressType", "InetAddress")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
NotificationType, Integer32, Counter32, TimeTicks, Gauge32, iso, Unsigned32, Counter64, ModuleIdentity, MibIdentifier, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "Integer32", "Counter32", "TimeTicks", "Gauge32", "iso", "Unsigned32", "Counter64", "ModuleIdentity", "MibIdentifier", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "IpAddress")
DisplayString, TextualConvention, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "RowStatus")
atIpMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 602))
atIpMib.setRevisions(('2010-06-14 05:09', '2008-11-10 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: atIpMib.setRevisionsDescriptions(('MIB revision history dates in descriptions updated.', 'Initial revision.',))
if mibBuilder.loadTexts: atIpMib.setLastUpdated('201006140509Z')
if mibBuilder.loadTexts: atIpMib.setOrganization('Allied Telesis Labs New Zealand')
if mibBuilder.loadTexts: atIpMib.setContactInfo('http://www.alliedtelesis.com')
if mibBuilder.loadTexts: atIpMib.setDescription('The IP MIB - for AT specific IP management.')
class AtIpAddressAssignmentType(TextualConvention, Integer32):
    description = 'The IP address assignment type being applied to the interface. notSet(0) indicates that the IP address assignment type has not yet been configured. This value can only ever be read. primary(1) indicates that the address is a primary IP address (only one primary address is allowed per interface). secondary(2) indicates that the address is a secondary IP address (any number of secondary IP addresses may be applied to each interface).'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("notSet", 0), ("primary", 1), ("secondary", 2))

atIpAddressTable = MibTable((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 602, 1), )
if mibBuilder.loadTexts: atIpAddressTable.setStatus('current')
if mibBuilder.loadTexts: atIpAddressTable.setDescription('A table containing mappings between primary/secondary IP addresses, and the interfaces they are assigned to.')
atIpAddressEntry = MibTableRow((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 602, 1, 1), ).setIndexNames((0, "AT-IP-MIB", "atIpAddressAddrType"), (0, "AT-IP-MIB", "atIpAddressAddr"))
if mibBuilder.loadTexts: atIpAddressEntry.setStatus('current')
if mibBuilder.loadTexts: atIpAddressEntry.setDescription('An address mapping for a particular interface.')
atIpAddressAddrType = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 602, 1, 1, 1), InetAddressType())
if mibBuilder.loadTexts: atIpAddressAddrType.setStatus('current')
if mibBuilder.loadTexts: atIpAddressAddrType.setDescription('An indication of the IP version of atIpAddressAddr.')
atIpAddressAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 602, 1, 1, 2), InetAddress())
if mibBuilder.loadTexts: atIpAddressAddr.setStatus('current')
if mibBuilder.loadTexts: atIpAddressAddr.setDescription("The IP address to which this entry's addressing information pertains. The address type of this object is specified in atIpAddressAddrType.")
atIpAddressPrefixLen = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 602, 1, 1, 3), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: atIpAddressPrefixLen.setStatus('current')
if mibBuilder.loadTexts: atIpAddressPrefixLen.setDescription('The prefix length of the IP address represented by this entry.')
atIpAddressLabel = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 602, 1, 1, 4), DisplayString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: atIpAddressLabel.setStatus('current')
if mibBuilder.loadTexts: atIpAddressLabel.setDescription('A name assigned to the IP address represented by this entry.')
atIpAddressIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 602, 1, 1, 5), InterfaceIndex()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: atIpAddressIfIndex.setStatus('current')
if mibBuilder.loadTexts: atIpAddressIfIndex.setDescription("The index value that uniquely identifies the interface to which this entry is applicable. The interface identified by a particular value of this index is the same interface as identified by the same value of the IF-MIB's ifIndex.")
atIpAddressAssignmentType = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 602, 1, 1, 6), AtIpAddressAssignmentType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: atIpAddressAssignmentType.setStatus('current')
if mibBuilder.loadTexts: atIpAddressAssignmentType.setDescription('The IP address assignment type for this entry (primary or secondary).')
atIpAddressRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 602, 1, 1, 7), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: atIpAddressRowStatus.setStatus('current')
if mibBuilder.loadTexts: atIpAddressRowStatus.setDescription('The current status of the IP address entry. The following values may be returned when reading this object: active (1) - The IP address is currently mapped to an interface and is valid. notReady (3) - The IP address is currently partially configured and is not mapped to an interface. The following values may be written to this object: active (1) - An attempt will be made to map the IP address to the configured interface. createAndWait (5) - An attempt will be made to create a new IP address entry. destroy (6) - The IP address setting will be removed from the device. An entry cannot be made active until its atIpAddressPrefixLen, atIpAddressIfIndex and atIpAddressAssignmentType objects have been set to valid values.')
mibBuilder.exportSymbols("AT-IP-MIB", atIpAddressTable=atIpAddressTable, atIpAddressAddrType=atIpAddressAddrType, atIpAddressAssignmentType=atIpAddressAssignmentType, atIpAddressLabel=atIpAddressLabel, atIpAddressAddr=atIpAddressAddr, atIpMib=atIpMib, atIpAddressRowStatus=atIpAddressRowStatus, atIpAddressIfIndex=atIpAddressIfIndex, PYSNMP_MODULE_ID=atIpMib, AtIpAddressAssignmentType=AtIpAddressAssignmentType, atIpAddressPrefixLen=atIpAddressPrefixLen, atIpAddressEntry=atIpAddressEntry)
