#
# PySNMP MIB module H3C-DAR-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/H3C-DAR-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:08:18 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint")
h3cCommon, = mibBuilder.importSymbols("HUAWEI-3COM-OID-MIB", "h3cCommon")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Unsigned32, iso, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, TimeTicks, IpAddress, Bits, Gauge32, ObjectIdentity, Integer32, Counter32, NotificationType, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "iso", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "TimeTicks", "IpAddress", "Bits", "Gauge32", "ObjectIdentity", "Integer32", "Counter32", "NotificationType", "MibIdentifier")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
h3cDar = ModuleIdentity((1, 3, 6, 1, 4, 1, 2011, 10, 2, 112))
if mibBuilder.loadTexts: h3cDar.setLastUpdated('201011030000Z')
if mibBuilder.loadTexts: h3cDar.setOrganization('Hangzhou H3C Technologies Co., Ltd.')
class H3cDarProtocol(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89))
    namedValues = NamedValues(("invalidProtocol", 1), ("bgp", 2), ("cifs", 3), ("citrix", 4), ("cuseeme", 5), ("dhcp", 6), ("dns", 7), ("egp", 8), ("eigrp", 9), ("exchange", 10), ("fasttrack", 11), ("finger", 12), ("ftp", 13), ("gnutella", 14), ("gopher", 15), ("gre", 16), ("http", 17), ("h323", 18), ("icmp", 19), ("igmp", 20), ("imap", 21), ("ip", 22), ("ipinip", 23), ("ipsec", 24), ("ipv6", 25), ("irc", 26), ("kerberos", 27), ("l2tp", 28), ("ldap", 29), ("mgcp", 30), ("napster", 31), ("netbios", 32), ("netshow", 33), ("nfs", 34), ("nntp", 35), ("notes", 36), ("novadign", 37), ("ntp", 38), ("pcanywhere", 39), ("pop3", 40), ("pptp", 41), ("printer", 42), ("rcmd", 43), ("rip", 44), ("rsvp", 45), ("rtcp", 46), ("rtp", 47), ("rtsp", 48), ("secureftp", 49), ("securehttp", 50), ("secureimap", 51), ("secureirc", 52), ("secureldap", 53), ("securenntp", 54), ("securepop3", 55), ("securetelnet", 56), ("sip", 57), ("skinny", 58), ("smtp", 59), ("snmp", 60), ("socks", 61), ("sqlnet", 62), ("sqlserver", 63), ("ssh", 64), ("streamwork", 65), ("sunrpc", 66), ("syslog", 67), ("tcp", 68), ("tcphandshake", 69), ("telnet", 70), ("tftp", 71), ("total", 72), ("udp", 73), ("unknownothers", 74), ("unknowntcp", 75), ("unknownudp", 76), ("userdefine001", 77), ("userdefine002", 78), ("userdefine003", 79), ("userdefine004", 80), ("userdefine005", 81), ("userdefine006", 82), ("userdefine007", 83), ("userdefine008", 84), ("userdefine009", 85), ("userdefine010", 86), ("vdolive", 87), ("winmx", 88), ("xwindows", 89))

h3cDarIfObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 2, 112, 1))
h3cDarIfStatisticsObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 2, 112, 1, 1))
h3cDarStatisticsTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 10, 2, 112, 1, 1, 1), )
if mibBuilder.loadTexts: h3cDarStatisticsTable.setStatus('current')
h3cDarStatisticsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 10, 2, 112, 1, 1, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "H3C-DAR-MIB", "h3cDarStatisticsProtocolID"))
if mibBuilder.loadTexts: h3cDarStatisticsEntry.setStatus('current')
h3cDarStatisticsProtocolID = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 112, 1, 1, 1, 1, 1), H3cDarProtocol())
if mibBuilder.loadTexts: h3cDarStatisticsProtocolID.setStatus('current')
h3cDarStatisticsProtocolName = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 112, 1, 1, 1, 1, 2), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cDarStatisticsProtocolName.setStatus('current')
h3cDarStatisticsInPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 112, 1, 1, 1, 1, 3), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cDarStatisticsInPkts.setStatus('current')
h3cDarStatisticsInBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 112, 1, 1, 1, 1, 4), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cDarStatisticsInBytes.setStatus('current')
h3cDarStatisticsInBitRate = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 112, 1, 1, 1, 1, 5), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cDarStatisticsInBitRate.setStatus('current')
h3cDarStatisticsMaxInBitRate = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 112, 1, 1, 1, 1, 6), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cDarStatisticsMaxInBitRate.setStatus('current')
h3cDarStatisticsOutPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 112, 1, 1, 1, 1, 7), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cDarStatisticsOutPkts.setStatus('current')
h3cDarStatisticsOutBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 112, 1, 1, 1, 1, 8), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cDarStatisticsOutBytes.setStatus('current')
h3cDarStatisticsOutBitRate = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 112, 1, 1, 1, 1, 9), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cDarStatisticsOutBitRate.setStatus('current')
h3cDarStatisticsMaxOutBitRate = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 112, 1, 1, 1, 1, 10), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cDarStatisticsMaxOutBitRate.setStatus('current')
mibBuilder.exportSymbols("H3C-DAR-MIB", h3cDar=h3cDar, H3cDarProtocol=H3cDarProtocol, PYSNMP_MODULE_ID=h3cDar, h3cDarStatisticsEntry=h3cDarStatisticsEntry, h3cDarStatisticsProtocolID=h3cDarStatisticsProtocolID, h3cDarStatisticsProtocolName=h3cDarStatisticsProtocolName, h3cDarStatisticsInBitRate=h3cDarStatisticsInBitRate, h3cDarStatisticsOutPkts=h3cDarStatisticsOutPkts, h3cDarStatisticsInBytes=h3cDarStatisticsInBytes, h3cDarStatisticsOutBytes=h3cDarStatisticsOutBytes, h3cDarStatisticsMaxOutBitRate=h3cDarStatisticsMaxOutBitRate, h3cDarStatisticsMaxInBitRate=h3cDarStatisticsMaxInBitRate, h3cDarStatisticsOutBitRate=h3cDarStatisticsOutBitRate, h3cDarIfObjects=h3cDarIfObjects, h3cDarStatisticsTable=h3cDarStatisticsTable, h3cDarIfStatisticsObjects=h3cDarIfStatisticsObjects, h3cDarStatisticsInPkts=h3cDarStatisticsInPkts)
