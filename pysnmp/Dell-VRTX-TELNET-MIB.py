#
# PySNMP MIB module Dell-VRTX-TELNET-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Dell-VRTX-TELNET-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:42:43 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection")
rnd, = mibBuilder.importSymbols("Dell-VRTX-MIB", "rnd")
InetAddressType, InetAddress = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressType", "InetAddress")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Gauge32, Counter32, MibIdentifier, iso, Bits, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, ObjectIdentity, TimeTicks, Counter64, ModuleIdentity, IpAddress, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "Counter32", "MibIdentifier", "iso", "Bits", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "ObjectIdentity", "TimeTicks", "Counter64", "ModuleIdentity", "IpAddress", "Unsigned32")
TruthValue, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "TextualConvention", "DisplayString")
rlTelnet = ModuleIdentity((1, 3, 6, 1, 4, 1, 89, 58))
rlTelnet.setRevisions(('2008-11-24 00:00',))
if mibBuilder.loadTexts: rlTelnet.setLastUpdated('200811240000Z')
if mibBuilder.loadTexts: rlTelnet.setOrganization('Dell')
rlTelnetMibVersion = MibScalar((1, 3, 6, 1, 4, 1, 89, 58, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlTelnetMibVersion.setStatus('current')
rlTelnetPassword = MibScalar((1, 3, 6, 1, 4, 1, 89, 58, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 20))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlTelnetPassword.setStatus('current')
rlTelnetTimeout = MibScalar((1, 3, 6, 1, 4, 1, 89, 58, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlTelnetTimeout.setStatus('current')
rlTelnetUsersTable = MibTable((1, 3, 6, 1, 4, 1, 89, 58, 4), )
if mibBuilder.loadTexts: rlTelnetUsersTable.setStatus('current')
rlTelnetUsersEntry = MibTableRow((1, 3, 6, 1, 4, 1, 89, 58, 4, 1), ).setIndexNames((0, "Dell-VRTX-TELNET-MIB", "rlTelnetSessionId"))
if mibBuilder.loadTexts: rlTelnetUsersEntry.setStatus('current')
rlTelnetSessionId = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 58, 4, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlTelnetSessionId.setStatus('current')
rlTelnetSessionClientAddressType = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 58, 4, 1, 2), InetAddressType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlTelnetSessionClientAddressType.setStatus('current')
rlTelnetSessionClientAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 58, 4, 1, 3), InetAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlTelnetSessionClientAddress.setStatus('current')
rlTelnetSessionLoginTime = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 58, 4, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlTelnetSessionLoginTime.setStatus('current')
rlTelnetSessionStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 58, 4, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("connected", 1), ("disconnect", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlTelnetSessionStatus.setStatus('current')
rlTelnetLoginBanner = MibScalar((1, 3, 6, 1, 4, 1, 89, 58, 5), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlTelnetLoginBanner.setStatus('current')
rlTelnetSecondLoginBanner = MibScalar((1, 3, 6, 1, 4, 1, 89, 58, 6), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlTelnetSecondLoginBanner.setStatus('current')
rlTelnetEnable = MibScalar((1, 3, 6, 1, 4, 1, 89, 58, 7), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlTelnetEnable.setStatus('current')
mibBuilder.exportSymbols("Dell-VRTX-TELNET-MIB", rlTelnetSessionId=rlTelnetSessionId, rlTelnetSessionClientAddressType=rlTelnetSessionClientAddressType, rlTelnetSecondLoginBanner=rlTelnetSecondLoginBanner, rlTelnetPassword=rlTelnetPassword, rlTelnetSessionLoginTime=rlTelnetSessionLoginTime, rlTelnetTimeout=rlTelnetTimeout, rlTelnetUsersEntry=rlTelnetUsersEntry, rlTelnetEnable=rlTelnetEnable, rlTelnetSessionStatus=rlTelnetSessionStatus, rlTelnetUsersTable=rlTelnetUsersTable, rlTelnet=rlTelnet, rlTelnetMibVersion=rlTelnetMibVersion, rlTelnetSessionClientAddress=rlTelnetSessionClientAddress, rlTelnetLoginBanner=rlTelnetLoginBanner, PYSNMP_MODULE_ID=rlTelnet)
