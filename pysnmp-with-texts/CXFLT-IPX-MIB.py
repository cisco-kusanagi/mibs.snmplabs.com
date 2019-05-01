#
# PySNMP MIB module CXFLT-IPX-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CXFLT-IPX-MIB
# Produced by pysmi-0.3.4 at Wed May  1 12:32:41 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint")
cxFltIpx, = mibBuilder.importSymbols("CXProduct-SMI", "cxFltIpx")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Bits, IpAddress, ModuleIdentity, ObjectIdentity, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, Counter64, Gauge32, MibIdentifier, Integer32, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "IpAddress", "ModuleIdentity", "ObjectIdentity", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "Counter64", "Gauge32", "MibIdentifier", "Integer32", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
class NetNumber(OctetString):
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(4, 4)
    fixedLength = 4

cxFltIpxAddrTable = MibTable((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 22, 1), )
if mibBuilder.loadTexts: cxFltIpxAddrTable.setStatus('mandatory')
if mibBuilder.loadTexts: cxFltIpxAddrTable.setDescription('Provides the filtering/forwarding information for each IPX address. Each entry (row) in the table corresponds to a specific IPX address. Some of the values in a row may be modified. If additional IPX addresses are required they may be added.')
cxFltIpxAddrEntry = MibTableRow((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 22, 1, 1), ).setIndexNames((0, "CXFLT-IPX-MIB", "cxFltIpxIndex"))
if mibBuilder.loadTexts: cxFltIpxAddrEntry.setStatus('mandatory')
if mibBuilder.loadTexts: cxFltIpxAddrEntry.setDescription('Provides the filtering/forwarding information for a specific IPX address.')
cxFltIpxIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 22, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cxFltIpxIndex.setStatus('mandatory')
if mibBuilder.loadTexts: cxFltIpxIndex.setDescription('Identifies the number used to index entries on the IPX filtering/forwarding table. The number provides access to all filtering/forwarding information for a source IPX address, its associated destination address, and filtering/forwarding parameter. Range of Values: 1-32 Default Value: None Configuration Changed: administrative')
cxFltIpxSrcAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 22, 1, 1, 2), NetNumber()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cxFltIpxSrcAddr.setStatus('mandatory')
if mibBuilder.loadTexts: cxFltIpxSrcAddr.setDescription('Determines the source IPX address (network number) used for filtering/forwarding. This address corresponds to a destination address in cxFltIpxDstAddr of this table. The object cxFltIpxParameter determines whether data is filtered or forwarded from the source address to the destination address. This number must be entered as 8 hexadecimal characters (four octets), for example 0xAB12CD34. The 0x must be present in every number; it indicates that the number is a hex number and is not counted as one of the octets. The x must be lowercase; the other characters are not case sensitive. Default Value: None Range of Values: 4 octets, each character ranging from 00 to FF Configuration Changed: administrative')
cxFltIpxDstAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 22, 1, 1, 3), NetNumber()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cxFltIpxDstAddr.setStatus('mandatory')
if mibBuilder.loadTexts: cxFltIpxDstAddr.setDescription('Determines the destination IPX address (network number). This address corresponds to a source address in cxFltIpxSrcAddr on this table. The object cxFltIpxParameter determines whether data is filtered or forwarded from the source address to this destination address. The address is an IPX network number. This number must be entered as 8 hexadecimal characters (four octets), for example 0xAB12CD34. The 0x must be present in every number; it indicates that the number is a hex number and is not counted as one of the octets. The x must be lowercase; the other characters are not case sensitive. Range of Values: 4 octets, each character ranging from 00 to FF Default Value: None Configuration Changed: administrative ')
cxFltIpxParameter = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 22, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("discard", 1), ("forward", 2), ("priority-low", 3), ("priority-high", 4))).clone('discard')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cxFltIpxParameter.setStatus('mandatory')
if mibBuilder.loadTexts: cxFltIpxParameter.setDescription('Determines the filtering/forwarding action and the priority processing for data sent from a source IPX address (cxFltIpxSrcAddr) to a destination IPX address (cxFltIpxDstAddr). Options: discard (1) forward (2) priority-low (3) priority-high (4) Default Value: discard (1) Configuration Changed: administrative ')
cxFltIpxRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 22, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("invalid", 1), ("valid", 2))).clone('valid')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cxFltIpxRowStatus.setStatus('mandatory')
if mibBuilder.loadTexts: cxFltIpxRowStatus.setDescription('Determines the status of the objects in a table row. Options: invalid (1): row is flagged, after the next reset, values are disabled and the row is deleted from the table. valid (2): values are enabled Default Value: valid (2) Configuration Changed: administrative')
mibBuilder.exportSymbols("CXFLT-IPX-MIB", cxFltIpxAddrEntry=cxFltIpxAddrEntry, cxFltIpxParameter=cxFltIpxParameter, NetNumber=NetNumber, cxFltIpxRowStatus=cxFltIpxRowStatus, cxFltIpxAddrTable=cxFltIpxAddrTable, cxFltIpxIndex=cxFltIpxIndex, cxFltIpxDstAddr=cxFltIpxDstAddr, cxFltIpxSrcAddr=cxFltIpxSrcAddr)
