#
# PySNMP MIB module S5-TCS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/S5-TCS-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:35:57 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
s5Tcs, = mibBuilder.importSymbols("S5-ROOT-MIB", "s5Tcs")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
ModuleIdentity, Counter64, NotificationType, Unsigned32, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, MibIdentifier, Bits, Counter32, iso, TimeTicks, Integer32, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "NotificationType", "Unsigned32", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "MibIdentifier", "Bits", "Counter32", "iso", "TimeTicks", "Integer32", "IpAddress")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
s5TcsMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 45, 1, 6, 17, 0))
s5TcsMib.setRevisions(('2013-10-10 00:00', '2004-07-20 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: s5TcsMib.setRevisionsDescriptions(('Version 114: Add Integer32 to IMPORTS.', 'Version 113: Conversion to SMIv2',))
if mibBuilder.loadTexts: s5TcsMib.setLastUpdated('201310100000Z')
if mibBuilder.loadTexts: s5TcsMib.setOrganization('Nortel Networks')
if mibBuilder.loadTexts: s5TcsMib.setContactInfo('Nortel Networks')
if mibBuilder.loadTexts: s5TcsMib.setDescription("5000 Common Textual Conventions MIB Copyright 1993-2004 Nortel Networks, Inc. All rights reserved. This Nortel Networks SNMP Management Information Base Specification (Specification) embodies Nortel Networks' confidential and proprietary intellectual property. Nortel Networks retains all title and ownership in the Specification, including any revisions. This Specification is supplied 'AS IS,' and Nortel Networks makes no warranty, either express or implied, as to the use, operation, condition, or performance of the Specification.")
class IpxAddress(TextualConvention, OctetString):
    description = "A textual convention for IPX addresses. The first four bytes are the network number in 'network order'. The last 6 bytes are the MAC address."
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(10, 10)
    fixedLength = 10

class TimeIntervalHrd(TextualConvention, Integer32):
    description = 'A textual convention for a period of time measured in units of 0.01 seconds.'
    status = 'current'

class TimeIntervalSec(TextualConvention, Integer32):
    description = 'A textual convention for a period of time measured in units of seconds.'
    status = 'current'

class SrcIndx(TextualConvention, Integer32):
    description = "A textual convention for an Index of a 'source'. The values are encoded so that the same MIB object can be used to describe the same type of data, but from different sources. For the 5000 Chassis, this is encoded in the following base 10 fields: 1bbiii - identifies an interface on an NMM where 'bb' is the board index and 'iii' is the interface number. 2bbppp - identifies a connectivity port on a board where 'bb' is the board INDEX and 'ppp' is the port INDEX. 3bblll - identifies a local channel on a board where 'bb' is the board INDEX and 'll' is the local channel INDEX. 4bbccc - identifies a cluster on a board where 'bb' is the board INDEX and 'cc' is the cluster INDEX. 5bbfff - identifies a FPU on a board where 'bb' is the board INDEX, and 'fff' is the FPU INDEX. 6bbnnn - identifies host board backplane counters where 'bb' is the board INDEX, and 'nnn' is the segment INDEX. 7bbccc - identifies a NULL segment on a board where 'bb' is the board INDEX, and 'ccc' is the cluster INDEX. 8mmnnn - identifies a sum across all host board(s) connected to a given backplane segment where 'mm' is media type, and 'nnn' is the segment INDEX. (NOTE: This is currently only valid for Ethernet.)"
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 999999)

class MediaType(TextualConvention, Integer32):
    description = 'A textual convention for Media types'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("other", 1), ("eth", 2), ("tok", 3), ("fddi", 4))

class FddiBkNetMode(TextualConvention, Integer32):
    description = 'The FDDI backplane mode.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("other", 1), ("thruLow", 2), ("thruHigh", 3), ("thruLowThruHigh", 4))

class BkNetId(TextualConvention, Integer32):
    description = 'The backplane network ID. This is a numeric assignment made to a backplane channel, a piece of a divided backplane channel, or a grouping of several backplane channels (which is done for FDDI). The number (and values) of the backplane networks is determined by the setting of the channel divider(s) which split some or all the backplane channels into networks, and by grouping when allowed by the media (such as FDDI). Different media and backplane implementations may have a divider or not. Also, there may be different mappings of backplane network IDs to a divided (or undivided) backplane channel. Note to agent implementors - you must map the divided (or undivided) backplane channel to the numbering here based on the setting of the backplane channel divider(s), and/or the grouping of the channels for FDDI.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 255)

class BkChan(TextualConvention, Integer32):
    description = 'The physical backplane channel identification. This does not change when a backplane is divided. A value of zero means no channel. Otherwise, the channels are numbered starting at one.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 255)

class LocChan(TextualConvention, Integer32):
    description = 'The physical local channel identification. A value of zero means no channel. Otherwise, the channels are numbered starting at one.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 255)

class AttId(TextualConvention, Integer32):
    description = 'The attachment ID. This is either a backplane network ID, a local channel, or as an indication of no backplane network attachment. Negative numbers are used to identify local channels on a board. Where used, the board must also be specified (or implied). A value of zero is used to indicate no (or null) attachment. Positive numbers are the backplane network IDs. The number (and values) of the backplane networks is determined by the setting of the channel divider(s) which split some or all the backplane channels into backplane networks, and by grouping when allowed by the media (such as FDDI). Different media and implementations may have a divider or not. Also, there may be different mappings of backplane network IDs to a divided (or undivided) backplane channel. Note to agent implementors - you must map the divided (or undivided) backplane channel to the numbering here based on the setting of the backplane channel divider(s), and/or the grouping of the channels for FDDI.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(-255, 255)

mibBuilder.exportSymbols("S5-TCS-MIB", TimeIntervalSec=TimeIntervalSec, MediaType=MediaType, IpxAddress=IpxAddress, TimeIntervalHrd=TimeIntervalHrd, LocChan=LocChan, SrcIndx=SrcIndx, AttId=AttId, PYSNMP_MODULE_ID=s5TcsMib, s5TcsMib=s5TcsMib, BkNetId=BkNetId, FddiBkNetMode=FddiBkNetMode, BkChan=BkChan)
