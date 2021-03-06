#
# PySNMP MIB module CISCO-CIPTG-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-CIPTG-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:35:59 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
SAPType, = mibBuilder.importSymbols("CISCO-TC", "SAPType")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
Unsigned32, Counter64, MibIdentifier, Bits, iso, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, ObjectIdentity, TimeTicks, Counter32, NotificationType, IpAddress, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "Counter64", "MibIdentifier", "Bits", "iso", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "ObjectIdentity", "TimeTicks", "Counter32", "NotificationType", "IpAddress", "ModuleIdentity")
DisplayString, TruthValue, MacAddress, TextualConvention, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TruthValue", "MacAddress", "TextualConvention", "RowStatus")
ciscoCipTgMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 73))
ciscoCipTgMIB.setRevisions(('1999-01-25 00:00', '1998-01-06 00:00', '1997-02-09 00:00', '1997-03-14 00:00',))
if mibBuilder.loadTexts: ciscoCipTgMIB.setLastUpdated('9901250000Z')
if mibBuilder.loadTexts: ciscoCipTgMIB.setOrganization('cisco IBU Engineering Working Group')
cipTgObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 73, 1))
cipTgLlc = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 73, 1, 1))
cipTgIp = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 73, 1, 2))
cipTgCmgr = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 73, 1, 3))
class ChannelTgName(DisplayString):
    status = 'current'
    subtypeSpec = DisplayString.subtypeSpec + ValueSizeConstraint(8, 8)
    fixedLength = 8

class ChannelTgToken(DisplayString):
    status = 'current'
    subtypeSpec = DisplayString.subtypeSpec + ValueSizeConstraint(0, 24)

cipTgLlcAdminTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 73, 1, 1, 1), )
if mibBuilder.loadTexts: cipTgLlcAdminTable.setStatus('current')
cipTgLlcAdminEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 73, 1, 1, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "CISCO-CIPTG-MIB", "cipTgLlcAdminName"))
if mibBuilder.loadTexts: cipTgLlcAdminEntry.setStatus('current')
cipTgLlcAdminName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 73, 1, 1, 1, 1, 1), ChannelTgName())
if mibBuilder.loadTexts: cipTgLlcAdminName.setStatus('current')
cipTgLlcAdminLanType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 73, 1, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("iso88023csmacd", 1), ("iso88025tokenRing", 2), ("fddi", 3)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cipTgLlcAdminLanType.setStatus('current')
cipTgLlcAdminAdaptNo = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 73, 1, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 31))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cipTgLlcAdminAdaptNo.setStatus('current')
cipTgLlcAdminLSAP = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 73, 1, 1, 1, 1, 4), SAPType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cipTgLlcAdminLSAP.setStatus('current')
cipTgLlcAdminRMAC = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 73, 1, 1, 1, 1, 5), MacAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cipTgLlcAdminRMAC.setStatus('current')
cipTgLlcAdminRSAP = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 73, 1, 1, 1, 1, 6), SAPType().clone(4)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cipTgLlcAdminRSAP.setStatus('current')
cipTgLlcAdminRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 73, 1, 1, 1, 1, 7), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cipTgLlcAdminRowStatus.setStatus('current')
cipTgLlcOperTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 73, 1, 1, 2), )
if mibBuilder.loadTexts: cipTgLlcOperTable.setStatus('current')
cipTgLlcOperEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 73, 1, 1, 2, 1), )
cipTgLlcAdminEntry.registerAugmentions(("CISCO-CIPTG-MIB", "cipTgLlcOperEntry"))
cipTgLlcOperEntry.setIndexNames(*cipTgLlcAdminEntry.getIndexNames())
if mibBuilder.loadTexts: cipTgLlcOperEntry.setStatus('current')
cipTgLlcOperState = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 73, 1, 1, 2, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))).clone(namedValues=NamedValues(("shutdown", 1), ("reset", 2), ("locatePeer", 3), ("peerLocated", 4), ("negotiation", 5), ("contactPending", 6), ("active", 7)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cipTgLlcOperState.setStatus('current')
cipTgLlcOperTGN = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 73, 1, 1, 2, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cipTgLlcOperTGN.setStatus('current')
cipTgLlcOperLocalCP = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 73, 1, 1, 2, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 17))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cipTgLlcOperLocalCP.setStatus('current')
cipTgLlcOperRemoteCP = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 73, 1, 1, 2, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 17))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cipTgLlcOperRemoteCP.setStatus('current')
cipTgLlcOperMaxIn = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 73, 1, 1, 2, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cipTgLlcOperMaxIn.setStatus('current')
cipTgLlcOperMaxOut = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 73, 1, 1, 2, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cipTgLlcOperMaxOut.setStatus('current')
cipTgLlcOperHpr = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 73, 1, 1, 2, 1, 7), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cipTgLlcOperHpr.setStatus('current')
cipTgLlcOperHprLSAP = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 73, 1, 1, 2, 1, 8), SAPType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cipTgLlcOperHprLSAP.setStatus('current')
cipTgLlcOperHprRSAP = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 73, 1, 1, 2, 1, 9), SAPType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cipTgLlcOperHprRSAP.setStatus('current')
cipTgLlcOperRIF = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 73, 1, 1, 2, 1, 10), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 18))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cipTgLlcOperRIF.setStatus('current')
cipTgLlcOperLocalVcToken = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 73, 1, 1, 2, 1, 11), ChannelTgToken()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cipTgLlcOperLocalVcToken.setStatus('current')
cipTgLlcOperRemoteVcToken = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 73, 1, 1, 2, 1, 12), ChannelTgToken()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cipTgLlcOperRemoteVcToken.setStatus('current')
cipTgLlcOperLocalConnToken = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 73, 1, 1, 2, 1, 13), ChannelTgToken()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cipTgLlcOperLocalConnToken.setStatus('current')
cipTgLlcOperRemoteConnToken = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 73, 1, 1, 2, 1, 14), ChannelTgToken()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cipTgLlcOperRemoteConnToken.setStatus('current')
cipTgLlcOperVcStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 73, 1, 1, 2, 1, 15), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("reset", 1), ("active", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cipTgLlcOperVcStatus.setStatus('current')
cipTgLlcOperConnStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 73, 1, 1, 2, 1, 16), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("reset", 1), ("connRequestSent", 2), ("pendingActive", 3), ("active", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cipTgLlcOperConnStatus.setStatus('current')
cipTgLlcStatsTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 73, 1, 1, 3), )
if mibBuilder.loadTexts: cipTgLlcStatsTable.setStatus('current')
cipTgLlcStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 73, 1, 1, 3, 1), )
cipTgLlcAdminEntry.registerAugmentions(("CISCO-CIPTG-MIB", "cipTgLlcStatsEntry"))
cipTgLlcStatsEntry.setIndexNames(*cipTgLlcAdminEntry.getIndexNames())
if mibBuilder.loadTexts: cipTgLlcStatsEntry.setStatus('current')
cipTgLlcStatsIFramesIn = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 73, 1, 1, 3, 1, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cipTgLlcStatsIFramesIn.setStatus('current')
cipTgLlcStatsIFrameBytesIn = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 73, 1, 1, 3, 1, 2), Counter32()).setUnits('octets').setMaxAccess("readonly")
if mibBuilder.loadTexts: cipTgLlcStatsIFrameBytesIn.setStatus('current')
cipTgLlcStatsHCIFrameBytesIn = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 73, 1, 1, 3, 1, 3), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cipTgLlcStatsHCIFrameBytesIn.setStatus('current')
cipTgLlcStatsIFramesOut = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 73, 1, 1, 3, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cipTgLlcStatsIFramesOut.setStatus('current')
cipTgLlcStatsIFrameBytesOut = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 73, 1, 1, 3, 1, 5), Counter32()).setUnits('octets').setMaxAccess("readonly")
if mibBuilder.loadTexts: cipTgLlcStatsIFrameBytesOut.setStatus('current')
cipTgLlcStatsHCIFrameBytesOut = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 73, 1, 1, 3, 1, 6), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cipTgLlcStatsHCIFrameBytesOut.setStatus('current')
cipTgLlcStatsUIFramesIn = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 73, 1, 1, 3, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cipTgLlcStatsUIFramesIn.setStatus('current')
cipTgLlcStatsUIFrameBytesIn = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 73, 1, 1, 3, 1, 8), Counter32()).setUnits('octets').setMaxAccess("readonly")
if mibBuilder.loadTexts: cipTgLlcStatsUIFrameBytesIn.setStatus('current')
cipTgLlcStatsHCUIFrameBytesIn = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 73, 1, 1, 3, 1, 9), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cipTgLlcStatsHCUIFrameBytesIn.setStatus('current')
cipTgLlcStatsUIFramesOut = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 73, 1, 1, 3, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cipTgLlcStatsUIFramesOut.setStatus('current')
cipTgLlcStatsUIFrameBytesOut = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 73, 1, 1, 3, 1, 11), Counter32()).setUnits('octets').setMaxAccess("readonly")
if mibBuilder.loadTexts: cipTgLlcStatsUIFrameBytesOut.setStatus('current')
cipTgLlcStatsHCUIFrameBytesOut = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 73, 1, 1, 3, 1, 12), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cipTgLlcStatsHCUIFrameBytesOut.setStatus('current')
cipTgLlcStatsTestCmdsOut = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 73, 1, 1, 3, 1, 13), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cipTgLlcStatsTestCmdsOut.setStatus('current')
cipTgLlcStatsTestRspsIn = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 73, 1, 1, 3, 1, 14), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cipTgLlcStatsTestRspsIn.setStatus('current')
cipTgLlcStatsXidCmdsIn = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 73, 1, 1, 3, 1, 15), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cipTgLlcStatsXidCmdsIn.setStatus('current')
cipTgLlcStatsXidCmdsOut = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 73, 1, 1, 3, 1, 16), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cipTgLlcStatsXidCmdsOut.setStatus('current')
cipTgLlcStatsXidRspsIn = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 73, 1, 1, 3, 1, 17), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cipTgLlcStatsXidRspsIn.setStatus('current')
cipTgLlcStatsXidRspsOut = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 73, 1, 1, 3, 1, 18), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cipTgLlcStatsXidRspsOut.setStatus('current')
cipTgLlcStatsConnNumberRecv = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 73, 1, 1, 3, 1, 19), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cipTgLlcStatsConnNumberRecv.setStatus('current')
cipTgLlcStatsConnNumberSent = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 73, 1, 1, 3, 1, 20), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cipTgLlcStatsConnNumberSent.setStatus('current')
cipTgIpAdminTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 73, 1, 2, 1), )
if mibBuilder.loadTexts: cipTgIpAdminTable.setStatus('current')
cipTgIpAdminEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 73, 1, 2, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "CISCO-CIPTG-MIB", "cipTgIpAdminName"))
if mibBuilder.loadTexts: cipTgIpAdminEntry.setStatus('current')
cipTgIpAdminName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 73, 1, 2, 1, 1, 1), ChannelTgName())
if mibBuilder.loadTexts: cipTgIpAdminName.setStatus('current')
cipTgIpAdminType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 73, 1, 2, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("tcpIp", 1), ("hsas", 2)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cipTgIpAdminType.setStatus('current')
cipTgIpAdminRemoteIpAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 73, 1, 2, 1, 1, 3), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cipTgIpAdminRemoteIpAddr.setStatus('current')
cipTgIpAdminLocalIpAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 73, 1, 2, 1, 1, 4), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cipTgIpAdminLocalIpAddr.setStatus('current')
cipTgIpAdminBroadcast = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 73, 1, 2, 1, 1, 5), TruthValue()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cipTgIpAdminBroadcast.setStatus('current')
cipTgIpAdminRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 73, 1, 2, 1, 1, 6), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cipTgIpAdminRowStatus.setStatus('current')
cipTgIpOperTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 73, 1, 2, 2), )
if mibBuilder.loadTexts: cipTgIpOperTable.setStatus('current')
cipTgIpOperEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 73, 1, 2, 2, 1), )
cipTgIpAdminEntry.registerAugmentions(("CISCO-CIPTG-MIB", "cipTgIpOperEntry"))
cipTgIpOperEntry.setIndexNames(*cipTgIpAdminEntry.getIndexNames())
if mibBuilder.loadTexts: cipTgIpOperEntry.setStatus('current')
cipTgIpOperLocalVcToken = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 73, 1, 2, 2, 1, 1), ChannelTgToken()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cipTgIpOperLocalVcToken.setStatus('current')
cipTgIpOperRemoteVcToken = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 73, 1, 2, 2, 1, 2), ChannelTgToken()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cipTgIpOperRemoteVcToken.setStatus('current')
cipTgIpOperLocalConnToken = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 73, 1, 2, 2, 1, 3), ChannelTgToken()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cipTgIpOperLocalConnToken.setStatus('current')
cipTgIpOperRemoteConnToken = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 73, 1, 2, 2, 1, 4), ChannelTgToken()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cipTgIpOperRemoteConnToken.setStatus('current')
cipTgIpOperVcStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 73, 1, 2, 2, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("reset", 1), ("active", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cipTgIpOperVcStatus.setStatus('current')
cipTgIpOperConnStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 73, 1, 2, 2, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("reset", 1), ("connRequestSent", 2), ("pendingActive", 3), ("active", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cipTgIpOperConnStatus.setStatus('current')
cipTgIpStatsTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 73, 1, 2, 3), )
if mibBuilder.loadTexts: cipTgIpStatsTable.setStatus('current')
cipTgIpStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 73, 1, 2, 3, 1), )
cipTgIpAdminEntry.registerAugmentions(("CISCO-CIPTG-MIB", "cipTgIpStatsEntry"))
cipTgIpStatsEntry.setIndexNames(*cipTgIpAdminEntry.getIndexNames())
if mibBuilder.loadTexts: cipTgIpStatsEntry.setStatus('current')
cipTgIpStatsPacketsIn = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 73, 1, 2, 3, 1, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cipTgIpStatsPacketsIn.setStatus('current')
cipTgIpStatsBytesIn = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 73, 1, 2, 3, 1, 2), Counter32()).setUnits('octets').setMaxAccess("readonly")
if mibBuilder.loadTexts: cipTgIpStatsBytesIn.setStatus('current')
cipTgIpStatsHCBytesIn = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 73, 1, 2, 3, 1, 3), Counter64()).setUnits('octets').setMaxAccess("readonly")
if mibBuilder.loadTexts: cipTgIpStatsHCBytesIn.setStatus('current')
cipTgIpStatsPacketsOut = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 73, 1, 2, 3, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cipTgIpStatsPacketsOut.setStatus('current')
cipTgIpStatsBytesOut = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 73, 1, 2, 3, 1, 5), Counter32()).setUnits('octets').setMaxAccess("readonly")
if mibBuilder.loadTexts: cipTgIpStatsBytesOut.setStatus('current')
cipTgIpStatsHCBytesOut = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 73, 1, 2, 3, 1, 6), Counter64()).setUnits('octets').setMaxAccess("readonly")
if mibBuilder.loadTexts: cipTgIpStatsHCBytesOut.setStatus('current')
cipTgCmgrOperTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 73, 1, 3, 1), )
if mibBuilder.loadTexts: cipTgCmgrOperTable.setStatus('current')
cipTgCmgrOperEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 73, 1, 3, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "CISCO-CIPTG-MIB", "cipTgCmgrOperName"))
if mibBuilder.loadTexts: cipTgCmgrOperEntry.setStatus('current')
cipTgCmgrOperName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 73, 1, 3, 1, 1, 1), ChannelTgName())
if mibBuilder.loadTexts: cipTgCmgrOperName.setStatus('current')
cipTgCmgrOperType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 73, 1, 3, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("pointToPoint", 1), ("pointToMultiPoint", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cipTgCmgrOperType.setStatus('current')
cipTgCmgrOperLocalGrToken = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 73, 1, 3, 1, 1, 3), ChannelTgToken()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cipTgCmgrOperLocalGrToken.setStatus('current')
cipTgCmgrOperRemoteGrToken = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 73, 1, 3, 1, 1, 4), ChannelTgToken()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cipTgCmgrOperRemoteGrToken.setStatus('current')
cipTgCmgrOperLocalVcToken = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 73, 1, 3, 1, 1, 5), ChannelTgToken()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cipTgCmgrOperLocalVcToken.setStatus('current')
cipTgCmgrOperRemoteVcToken = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 73, 1, 3, 1, 1, 6), ChannelTgToken()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cipTgCmgrOperRemoteVcToken.setStatus('current')
cipTgCmgrOperLocalConnToken = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 73, 1, 3, 1, 1, 7), ChannelTgToken()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cipTgCmgrOperLocalConnToken.setStatus('current')
cipTgCmgrOperRemoteConnToken = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 73, 1, 3, 1, 1, 8), ChannelTgToken()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cipTgCmgrOperRemoteConnToken.setStatus('current')
cipTgCmgrOperVcStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 73, 1, 3, 1, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("reset", 1), ("active", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cipTgCmgrOperVcStatus.setStatus('current')
cipTgCmgrOperConnStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 73, 1, 3, 1, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("reset", 1), ("active", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cipTgCmgrOperConnStatus.setStatus('current')
ciscoCipTgMibConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 73, 3))
ciscoCipTgMibCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 73, 3, 1))
ciscoCipTgMibGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 73, 3, 2))
ciscoCipTgMibCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 73, 3, 1, 1)).setObjects(("CISCO-CIPTG-MIB", "ciscoCipTgLlcGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCipTgMibCompliance = ciscoCipTgMibCompliance.setStatus('obsolete')
ciscoCipTgMibComplianceRev1 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 73, 3, 1, 2)).setObjects(("CISCO-CIPTG-MIB", "ciscoCipTgLlcGroupRev1"), ("CISCO-CIPTG-MIB", "ciscoCipTgIpGroup"), ("CISCO-CIPTG-MIB", "ciscoCipTgCmgrGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCipTgMibComplianceRev1 = ciscoCipTgMibComplianceRev1.setStatus('current')
ciscoCipTgLlcGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 73, 3, 2, 2)).setObjects(("CISCO-CIPTG-MIB", "cipTgLlcAdminLanType"), ("CISCO-CIPTG-MIB", "cipTgLlcAdminAdaptNo"), ("CISCO-CIPTG-MIB", "cipTgLlcAdminLSAP"), ("CISCO-CIPTG-MIB", "cipTgLlcAdminRMAC"), ("CISCO-CIPTG-MIB", "cipTgLlcAdminRSAP"), ("CISCO-CIPTG-MIB", "cipTgLlcAdminRowStatus"), ("CISCO-CIPTG-MIB", "cipTgLlcOperState"), ("CISCO-CIPTG-MIB", "cipTgLlcOperTGN"), ("CISCO-CIPTG-MIB", "cipTgLlcOperLocalCP"), ("CISCO-CIPTG-MIB", "cipTgLlcOperRemoteCP"), ("CISCO-CIPTG-MIB", "cipTgLlcOperMaxIn"), ("CISCO-CIPTG-MIB", "cipTgLlcOperMaxOut"), ("CISCO-CIPTG-MIB", "cipTgLlcOperHpr"), ("CISCO-CIPTG-MIB", "cipTgLlcOperHprLSAP"), ("CISCO-CIPTG-MIB", "cipTgLlcOperHprRSAP"), ("CISCO-CIPTG-MIB", "cipTgLlcOperRIF"), ("CISCO-CIPTG-MIB", "cipTgLlcStatsIFramesIn"), ("CISCO-CIPTG-MIB", "cipTgLlcStatsIFrameBytesIn"), ("CISCO-CIPTG-MIB", "cipTgLlcStatsHCIFrameBytesIn"), ("CISCO-CIPTG-MIB", "cipTgLlcStatsIFramesOut"), ("CISCO-CIPTG-MIB", "cipTgLlcStatsIFrameBytesOut"), ("CISCO-CIPTG-MIB", "cipTgLlcStatsHCIFrameBytesOut"), ("CISCO-CIPTG-MIB", "cipTgLlcStatsUIFramesIn"), ("CISCO-CIPTG-MIB", "cipTgLlcStatsUIFrameBytesIn"), ("CISCO-CIPTG-MIB", "cipTgLlcStatsHCUIFrameBytesIn"), ("CISCO-CIPTG-MIB", "cipTgLlcStatsUIFramesOut"), ("CISCO-CIPTG-MIB", "cipTgLlcStatsUIFrameBytesOut"), ("CISCO-CIPTG-MIB", "cipTgLlcStatsHCUIFrameBytesOut"), ("CISCO-CIPTG-MIB", "cipTgLlcStatsTestCmdsOut"), ("CISCO-CIPTG-MIB", "cipTgLlcStatsTestRspsIn"), ("CISCO-CIPTG-MIB", "cipTgLlcStatsXidCmdsIn"), ("CISCO-CIPTG-MIB", "cipTgLlcStatsXidCmdsOut"), ("CISCO-CIPTG-MIB", "cipTgLlcStatsXidRspsIn"), ("CISCO-CIPTG-MIB", "cipTgLlcStatsXidRspsOut"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCipTgLlcGroup = ciscoCipTgLlcGroup.setStatus('obsolete')
ciscoCipTgLlcGroupRev1 = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 73, 3, 2, 3)).setObjects(("CISCO-CIPTG-MIB", "cipTgLlcAdminLanType"), ("CISCO-CIPTG-MIB", "cipTgLlcAdminAdaptNo"), ("CISCO-CIPTG-MIB", "cipTgLlcAdminLSAP"), ("CISCO-CIPTG-MIB", "cipTgLlcAdminRMAC"), ("CISCO-CIPTG-MIB", "cipTgLlcAdminRSAP"), ("CISCO-CIPTG-MIB", "cipTgLlcAdminRowStatus"), ("CISCO-CIPTG-MIB", "cipTgLlcOperState"), ("CISCO-CIPTG-MIB", "cipTgLlcOperTGN"), ("CISCO-CIPTG-MIB", "cipTgLlcOperLocalCP"), ("CISCO-CIPTG-MIB", "cipTgLlcOperRemoteCP"), ("CISCO-CIPTG-MIB", "cipTgLlcOperMaxIn"), ("CISCO-CIPTG-MIB", "cipTgLlcOperMaxOut"), ("CISCO-CIPTG-MIB", "cipTgLlcOperHpr"), ("CISCO-CIPTG-MIB", "cipTgLlcOperHprLSAP"), ("CISCO-CIPTG-MIB", "cipTgLlcOperHprRSAP"), ("CISCO-CIPTG-MIB", "cipTgLlcOperRIF"), ("CISCO-CIPTG-MIB", "cipTgLlcOperLocalVcToken"), ("CISCO-CIPTG-MIB", "cipTgLlcOperRemoteVcToken"), ("CISCO-CIPTG-MIB", "cipTgLlcOperLocalConnToken"), ("CISCO-CIPTG-MIB", "cipTgLlcOperRemoteConnToken"), ("CISCO-CIPTG-MIB", "cipTgLlcOperVcStatus"), ("CISCO-CIPTG-MIB", "cipTgLlcOperConnStatus"), ("CISCO-CIPTG-MIB", "cipTgLlcStatsIFramesIn"), ("CISCO-CIPTG-MIB", "cipTgLlcStatsIFrameBytesIn"), ("CISCO-CIPTG-MIB", "cipTgLlcStatsHCIFrameBytesIn"), ("CISCO-CIPTG-MIB", "cipTgLlcStatsIFramesOut"), ("CISCO-CIPTG-MIB", "cipTgLlcStatsIFrameBytesOut"), ("CISCO-CIPTG-MIB", "cipTgLlcStatsHCIFrameBytesOut"), ("CISCO-CIPTG-MIB", "cipTgLlcStatsUIFramesIn"), ("CISCO-CIPTG-MIB", "cipTgLlcStatsUIFrameBytesIn"), ("CISCO-CIPTG-MIB", "cipTgLlcStatsHCUIFrameBytesIn"), ("CISCO-CIPTG-MIB", "cipTgLlcStatsUIFramesOut"), ("CISCO-CIPTG-MIB", "cipTgLlcStatsUIFrameBytesOut"), ("CISCO-CIPTG-MIB", "cipTgLlcStatsHCUIFrameBytesOut"), ("CISCO-CIPTG-MIB", "cipTgLlcStatsTestCmdsOut"), ("CISCO-CIPTG-MIB", "cipTgLlcStatsTestRspsIn"), ("CISCO-CIPTG-MIB", "cipTgLlcStatsXidCmdsIn"), ("CISCO-CIPTG-MIB", "cipTgLlcStatsXidCmdsOut"), ("CISCO-CIPTG-MIB", "cipTgLlcStatsXidRspsIn"), ("CISCO-CIPTG-MIB", "cipTgLlcStatsXidRspsOut"), ("CISCO-CIPTG-MIB", "cipTgLlcStatsConnNumberRecv"), ("CISCO-CIPTG-MIB", "cipTgLlcStatsConnNumberSent"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCipTgLlcGroupRev1 = ciscoCipTgLlcGroupRev1.setStatus('current')
ciscoCipTgIpGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 73, 3, 2, 4)).setObjects(("CISCO-CIPTG-MIB", "cipTgIpAdminType"), ("CISCO-CIPTG-MIB", "cipTgIpAdminRemoteIpAddr"), ("CISCO-CIPTG-MIB", "cipTgIpAdminLocalIpAddr"), ("CISCO-CIPTG-MIB", "cipTgIpAdminBroadcast"), ("CISCO-CIPTG-MIB", "cipTgIpAdminRowStatus"), ("CISCO-CIPTG-MIB", "cipTgIpOperLocalVcToken"), ("CISCO-CIPTG-MIB", "cipTgIpOperRemoteVcToken"), ("CISCO-CIPTG-MIB", "cipTgIpOperLocalConnToken"), ("CISCO-CIPTG-MIB", "cipTgIpOperRemoteConnToken"), ("CISCO-CIPTG-MIB", "cipTgIpOperVcStatus"), ("CISCO-CIPTG-MIB", "cipTgIpOperConnStatus"), ("CISCO-CIPTG-MIB", "cipTgIpStatsPacketsIn"), ("CISCO-CIPTG-MIB", "cipTgIpStatsBytesIn"), ("CISCO-CIPTG-MIB", "cipTgIpStatsHCBytesIn"), ("CISCO-CIPTG-MIB", "cipTgIpStatsPacketsOut"), ("CISCO-CIPTG-MIB", "cipTgIpStatsBytesOut"), ("CISCO-CIPTG-MIB", "cipTgIpStatsHCBytesOut"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCipTgIpGroup = ciscoCipTgIpGroup.setStatus('current')
ciscoCipTgCmgrGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 73, 3, 2, 5)).setObjects(("CISCO-CIPTG-MIB", "cipTgCmgrOperType"), ("CISCO-CIPTG-MIB", "cipTgCmgrOperLocalGrToken"), ("CISCO-CIPTG-MIB", "cipTgCmgrOperRemoteGrToken"), ("CISCO-CIPTG-MIB", "cipTgCmgrOperLocalVcToken"), ("CISCO-CIPTG-MIB", "cipTgCmgrOperRemoteVcToken"), ("CISCO-CIPTG-MIB", "cipTgCmgrOperLocalConnToken"), ("CISCO-CIPTG-MIB", "cipTgCmgrOperRemoteConnToken"), ("CISCO-CIPTG-MIB", "cipTgCmgrOperVcStatus"), ("CISCO-CIPTG-MIB", "cipTgCmgrOperConnStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCipTgCmgrGroup = ciscoCipTgCmgrGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-CIPTG-MIB", cipTgLlcOperTable=cipTgLlcOperTable, cipTgLlcAdminTable=cipTgLlcAdminTable, cipTgLlcOperRemoteCP=cipTgLlcOperRemoteCP, cipTgLlcStatsEntry=cipTgLlcStatsEntry, cipTgIpOperTable=cipTgIpOperTable, cipTgLlcStatsTestCmdsOut=cipTgLlcStatsTestCmdsOut, ChannelTgToken=ChannelTgToken, cipTgLlcOperVcStatus=cipTgLlcOperVcStatus, cipTgCmgrOperTable=cipTgCmgrOperTable, cipTgLlcStatsHCIFrameBytesOut=cipTgLlcStatsHCIFrameBytesOut, cipTgCmgrOperLocalGrToken=cipTgCmgrOperLocalGrToken, cipTgIpStatsEntry=cipTgIpStatsEntry, cipTgLlcOperConnStatus=cipTgLlcOperConnStatus, cipTgLlcOperHpr=cipTgLlcOperHpr, cipTgLlcAdminRMAC=cipTgLlcAdminRMAC, cipTgObjects=cipTgObjects, cipTgCmgrOperVcStatus=cipTgCmgrOperVcStatus, cipTgLlcOperHprRSAP=cipTgLlcOperHprRSAP, cipTgLlcStatsTestRspsIn=cipTgLlcStatsTestRspsIn, cipTgIpStatsHCBytesIn=cipTgIpStatsHCBytesIn, cipTgLlcStatsXidCmdsOut=cipTgLlcStatsXidCmdsOut, ChannelTgName=ChannelTgName, cipTgIpStatsPacketsOut=cipTgIpStatsPacketsOut, cipTgLlcOperLocalConnToken=cipTgLlcOperLocalConnToken, cipTgLlcStatsUIFramesIn=cipTgLlcStatsUIFramesIn, cipTgIpOperRemoteVcToken=cipTgIpOperRemoteVcToken, cipTgIpAdminType=cipTgIpAdminType, cipTgIpOperRemoteConnToken=cipTgIpOperRemoteConnToken, ciscoCipTgIpGroup=ciscoCipTgIpGroup, cipTgLlcStatsIFrameBytesOut=cipTgLlcStatsIFrameBytesOut, cipTgCmgrOperConnStatus=cipTgCmgrOperConnStatus, cipTgLlcAdminName=cipTgLlcAdminName, cipTgLlcOperMaxOut=cipTgLlcOperMaxOut, ciscoCipTgMibComplianceRev1=ciscoCipTgMibComplianceRev1, cipTgIpOperConnStatus=cipTgIpOperConnStatus, cipTgLlcOperRemoteVcToken=cipTgLlcOperRemoteVcToken, cipTgCmgrOperRemoteConnToken=cipTgCmgrOperRemoteConnToken, cipTgIpStatsBytesIn=cipTgIpStatsBytesIn, cipTgLlcOperRemoteConnToken=cipTgLlcOperRemoteConnToken, cipTgLlcOperEntry=cipTgLlcOperEntry, cipTgIpStatsTable=cipTgIpStatsTable, ciscoCipTgCmgrGroup=ciscoCipTgCmgrGroup, cipTgLlcStatsXidRspsIn=cipTgLlcStatsXidRspsIn, cipTgLlcOperState=cipTgLlcOperState, cipTgLlcStatsUIFramesOut=cipTgLlcStatsUIFramesOut, cipTgLlcStatsTable=cipTgLlcStatsTable, cipTgCmgrOperEntry=cipTgCmgrOperEntry, cipTgLlcStatsHCIFrameBytesIn=cipTgLlcStatsHCIFrameBytesIn, cipTgIpAdminRemoteIpAddr=cipTgIpAdminRemoteIpAddr, cipTgIp=cipTgIp, cipTgCmgrOperRemoteGrToken=cipTgCmgrOperRemoteGrToken, cipTgIpOperVcStatus=cipTgIpOperVcStatus, cipTgLlc=cipTgLlc, cipTgLlcOperRIF=cipTgLlcOperRIF, ciscoCipTgMibCompliance=ciscoCipTgMibCompliance, cipTgLlcStatsIFramesOut=cipTgLlcStatsIFramesOut, cipTgCmgrOperRemoteVcToken=cipTgCmgrOperRemoteVcToken, cipTgIpOperLocalVcToken=cipTgIpOperLocalVcToken, cipTgLlcStatsXidCmdsIn=cipTgLlcStatsXidCmdsIn, cipTgCmgrOperLocalConnToken=cipTgCmgrOperLocalConnToken, cipTgLlcAdminRSAP=cipTgLlcAdminRSAP, cipTgLlcOperMaxIn=cipTgLlcOperMaxIn, ciscoCipTgLlcGroupRev1=ciscoCipTgLlcGroupRev1, cipTgIpOperLocalConnToken=cipTgIpOperLocalConnToken, cipTgIpStatsPacketsIn=cipTgIpStatsPacketsIn, cipTgLlcStatsHCUIFrameBytesOut=cipTgLlcStatsHCUIFrameBytesOut, cipTgIpStatsBytesOut=cipTgIpStatsBytesOut, cipTgIpAdminLocalIpAddr=cipTgIpAdminLocalIpAddr, cipTgIpAdminName=cipTgIpAdminName, cipTgLlcAdminRowStatus=cipTgLlcAdminRowStatus, cipTgLlcOperHprLSAP=cipTgLlcOperHprLSAP, cipTgIpAdminRowStatus=cipTgIpAdminRowStatus, ciscoCipTgMibConformance=ciscoCipTgMibConformance, ciscoCipTgMibCompliances=ciscoCipTgMibCompliances, cipTgLlcStatsConnNumberSent=cipTgLlcStatsConnNumberSent, cipTgIpAdminTable=cipTgIpAdminTable, cipTgLlcAdminAdaptNo=cipTgLlcAdminAdaptNo, cipTgLlcAdminEntry=cipTgLlcAdminEntry, cipTgIpOperEntry=cipTgIpOperEntry, cipTgCmgrOperName=cipTgCmgrOperName, cipTgLlcStatsIFramesIn=cipTgLlcStatsIFramesIn, cipTgIpAdminBroadcast=cipTgIpAdminBroadcast, cipTgLlcStatsUIFrameBytesIn=cipTgLlcStatsUIFrameBytesIn, cipTgLlcOperTGN=cipTgLlcOperTGN, ciscoCipTgLlcGroup=ciscoCipTgLlcGroup, cipTgLlcOperLocalCP=cipTgLlcOperLocalCP, cipTgLlcStatsUIFrameBytesOut=cipTgLlcStatsUIFrameBytesOut, cipTgLlcStatsIFrameBytesIn=cipTgLlcStatsIFrameBytesIn, ciscoCipTgMIB=ciscoCipTgMIB, ciscoCipTgMibGroups=ciscoCipTgMibGroups, cipTgLlcStatsHCUIFrameBytesIn=cipTgLlcStatsHCUIFrameBytesIn, cipTgLlcStatsConnNumberRecv=cipTgLlcStatsConnNumberRecv, cipTgCmgrOperType=cipTgCmgrOperType, cipTgLlcAdminLanType=cipTgLlcAdminLanType, cipTgIpStatsHCBytesOut=cipTgIpStatsHCBytesOut, cipTgCmgr=cipTgCmgr, cipTgLlcStatsXidRspsOut=cipTgLlcStatsXidRspsOut, cipTgLlcAdminLSAP=cipTgLlcAdminLSAP, cipTgLlcOperLocalVcToken=cipTgLlcOperLocalVcToken, PYSNMP_MODULE_ID=ciscoCipTgMIB, cipTgIpAdminEntry=cipTgIpAdminEntry, cipTgCmgrOperLocalVcToken=cipTgCmgrOperLocalVcToken)
