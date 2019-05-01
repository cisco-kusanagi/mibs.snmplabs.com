#
# PySNMP MIB module RMON2-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/RMON2-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:05:00 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
matrix, hosts, history, filter, matrixControlEntry, statistics, filterEntry, historyControlEntry, hostControlEntry, channelEntry, etherStatsEntry, OwnerString = mibBuilder.importSymbols("RMON-MIB", "matrix", "hosts", "history", "filter", "matrixControlEntry", "statistics", "filterEntry", "historyControlEntry", "hostControlEntry", "channelEntry", "etherStatsEntry", "OwnerString")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ObjectIdentity, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, Integer32, Counter64, Counter32, ModuleIdentity, iso, Unsigned32, MibIdentifier, Gauge32, mib_2, IpAddress, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "Integer32", "Counter64", "Counter32", "ModuleIdentity", "iso", "Unsigned32", "MibIdentifier", "Gauge32", "mib-2", "IpAddress", "TimeTicks")
TimeStamp, DisplayString, RowStatus, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "TimeStamp", "DisplayString", "RowStatus", "TextualConvention")
rmon = ModuleIdentity((1, 3, 6, 1, 2, 1, 16))
if mibBuilder.loadTexts: rmon.setLastUpdated('9605270000Z')
if mibBuilder.loadTexts: rmon.setOrganization('IETF RMON MIB Working Group')
if mibBuilder.loadTexts: rmon.setContactInfo('Steve Waldbusser (WG Editor) Postal: International Network Services 650 Castro Street, Suite 260 Mountain View, CA 94041 Phone: +1 415 254 4251 Email: waldbusser@ins.com Andy Bierman (WG Chair) Phone: +1 805 648 2028 Email: abierman@west.net')
if mibBuilder.loadTexts: rmon.setDescription('The MIB module for managing remote monitoring device implementations. This MIB module augments the original RMON MIB as specified in RFC 1757.')
protocolDir = MibIdentifier((1, 3, 6, 1, 2, 1, 16, 11))
protocolDist = MibIdentifier((1, 3, 6, 1, 2, 1, 16, 12))
addressMap = MibIdentifier((1, 3, 6, 1, 2, 1, 16, 13))
nlHost = MibIdentifier((1, 3, 6, 1, 2, 1, 16, 14))
nlMatrix = MibIdentifier((1, 3, 6, 1, 2, 1, 16, 15))
alHost = MibIdentifier((1, 3, 6, 1, 2, 1, 16, 16))
alMatrix = MibIdentifier((1, 3, 6, 1, 2, 1, 16, 17))
usrHistory = MibIdentifier((1, 3, 6, 1, 2, 1, 16, 18))
probeConfig = MibIdentifier((1, 3, 6, 1, 2, 1, 16, 19))
rmonConformance = MibIdentifier((1, 3, 6, 1, 2, 1, 16, 20))
class ZeroBasedCounter32(TextualConvention, Gauge32):
    description = 'This TC describes an object which counts events with the following semantics: objects of this type will be set to zero(0) on creation and will thereafter count appropriate events, wrapping back to zero(0) when the value 2^32 is reached. Provided that an application discovers the new object within the minimum time to wrap it can use the initial value as a delta since it last polled the table of which this object is part. It is important for a management station to be aware of this minimum time and the actual time between polls, and to discard data if the actual time is too long or there is no defined minimum time. Typically this TC is used in tables where the INDEX space is constantly changing and/or the TimeFilter mechanism is in use.'
    status = 'current'

class LastCreateTime(TimeStamp):
    description = 'This TC describes an object that stores the last time its entry was created. This can be used for polling applications to determine that an entry has been deleted and re-created between polls, causing an otherwise undetectable discontinuity in the data.'
    status = 'current'

class TimeFilter(TextualConvention, TimeTicks):
    description = "To be used for the index to a table. Allows an application to download only those rows changed since a particular time. A row is considered changed if the value of any object in the row changes or if the row is created or deleted. When sysUpTime is equal to zero, this table shall be empty. One entry exists for each past value of sysUpTime, except that the whole table is purged should sysUpTime wrap. As this basic row is updated new conceptual rows are created (which still share the now updated object values with all other instances). The number of instances which are created is determined by the value of sysUpTime at which the basic row was last updated. One instance will exist for each value of sysUpTime at the last update time for the row. A new timeMark instance is created for each new sysUpTime value. Each new conceptual row will be associated with the timeMark instance which was created at the value of sysUpTime with which the conceptual row is to be associated. By definition all conceptual rows were updated at or after time zero and so at least one conceptual row (associated with timeMark.0) must exist for each underlying (basic) row. See the appendix for further discussion of this variable. Consider the following fooTable: fooTable ... INDEX { fooTimeMark, fooIndex } FooEntry { fooTimeMark TimeFilter fooIndex INTEGER, fooCounts Counter } Should there be two basic rows in this table (fooIndex == 1, fooIndex == 2) and row 1 was updated most recently at time 6, while row 2 was updated most recently at time 8, and both rows had been updated on several earlier occasions such that the current values were 5 and 9 respectively then the following fooCounts instances would exist. fooCounts.0.1 5 fooCounts.0.2 9 fooCounts.1.1 5 fooCounts.1.2 9 fooCounts.2.1 5 fooCounts.2.2 9 fooCounts.3.1 5 fooCounts.3.2 9 fooCounts.4.1 5 fooCounts.4.2 9 fooCounts.5.1 5 fooCounts.5.2 9 fooCounts.6.1 5 fooCounts.6.2 9 fooCounts.7.2 9 -- note that row 1 doesn't exist for fooCounts.8.2 9 -- times 7 and 8"
    status = 'current'

class DataSource(TextualConvention, ObjectIdentifier):
    description = 'Identifies the source of the data that the associated function is configured to analyze. This source can be any interface on this device. In order to identify a particular interface, this object shall identify the instance of the ifIndex object, defined in [3,5], for the desired interface. For example, if an entry were to receive data from interface #1, this object would be set to ifIndex.1.'
    status = 'current'

mibBuilder.exportSymbols("RMON2-MIB", addressMap=addressMap, rmon=rmon, LastCreateTime=LastCreateTime, alMatrix=alMatrix, usrHistory=usrHistory, PYSNMP_MODULE_ID=rmon, ZeroBasedCounter32=ZeroBasedCounter32, nlMatrix=nlMatrix, alHost=alHost, TimeFilter=TimeFilter, protocolDir=protocolDir, nlHost=nlHost, DataSource=DataSource, protocolDist=protocolDist, probeConfig=probeConfig, rmonConformance=rmonConformance)
