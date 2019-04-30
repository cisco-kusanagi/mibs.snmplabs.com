#
# PySNMP MIB module RMON2-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/RMON2-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 16:50:13 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
channelEntry, hosts, filter, etherStatsEntry, historyControlEntry, matrixControlEntry, statistics, OwnerString, history, matrix, filterEntry, hostControlEntry = mibBuilder.importSymbols("RMON-MIB", "channelEntry", "hosts", "filter", "etherStatsEntry", "historyControlEntry", "matrixControlEntry", "statistics", "OwnerString", "history", "matrix", "filterEntry", "hostControlEntry")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
mib_2, Counter32, TimeTicks, ObjectIdentity, ModuleIdentity, MibIdentifier, iso, Counter64, Bits, Integer32, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, NotificationType, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "mib-2", "Counter32", "TimeTicks", "ObjectIdentity", "ModuleIdentity", "MibIdentifier", "iso", "Counter64", "Bits", "Integer32", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "NotificationType", "Gauge32")
TimeStamp, TextualConvention, RowStatus, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TimeStamp", "TextualConvention", "RowStatus", "DisplayString")
rmon = ModuleIdentity((1, 3, 6, 1, 2, 1, 16))
if mibBuilder.loadTexts: rmon.setLastUpdated('9605270000Z')
if mibBuilder.loadTexts: rmon.setOrganization('IETF RMON MIB Working Group')
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
    status = 'current'

class LastCreateTime(TimeStamp):
    status = 'current'

class TimeFilter(TextualConvention, TimeTicks):
    status = 'current'

class DataSource(TextualConvention, ObjectIdentifier):
    status = 'current'

mibBuilder.exportSymbols("RMON2-MIB", LastCreateTime=LastCreateTime, addressMap=addressMap, PYSNMP_MODULE_ID=rmon, rmon=rmon, alHost=alHost, protocolDir=protocolDir, probeConfig=probeConfig, alMatrix=alMatrix, usrHistory=usrHistory, ZeroBasedCounter32=ZeroBasedCounter32, TimeFilter=TimeFilter, rmonConformance=rmonConformance, nlHost=nlHost, nlMatrix=nlMatrix, DataSource=DataSource, protocolDist=protocolDist)
