#
# PySNMP MIB module NETSCREEN-USER-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/NETSCREEN-USER-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:20:31 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint")
netscreenVpn, = mibBuilder.importSymbols("NETSCREEN-SMI", "netscreenVpn")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
ModuleIdentity, Integer32, Counter64, iso, Counter32, Gauge32, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, MibIdentifier, TimeTicks, ObjectIdentity, IpAddress, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Integer32", "Counter64", "iso", "Counter32", "Gauge32", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "MibIdentifier", "TimeTicks", "ObjectIdentity", "IpAddress", "NotificationType")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
nsVpnUser = MibIdentifier((1, 3, 6, 1, 4, 1, 3224, 4, 10))
nsVpnUsrDialupGrpTable = MibTable((1, 3, 6, 1, 4, 1, 3224, 4, 10, 1), )
if mibBuilder.loadTexts: nsVpnUsrDialupGrpTable.setStatus('mandatory')
if mibBuilder.loadTexts: nsVpnUsrDialupGrpTable.setDescription('NetScreen supports using dialup group to organize vpn user.This table collects the information of dialup group in NetScreen device.')
nsVpnUsrDialupGrpEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3224, 4, 10, 1, 1), ).setIndexNames((0, "NETSCREEN-USER-MIB", "nsVpnUsrDialupGrpIndex"))
if mibBuilder.loadTexts: nsVpnUsrDialupGrpEntry.setStatus('mandatory')
if mibBuilder.loadTexts: nsVpnUsrDialupGrpEntry.setDescription('Each entry in this table holds a set of configuration information about dialup group.')
nsVpnUsrDialupGrpIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 3224, 4, 10, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsVpnUsrDialupGrpIndex.setStatus('mandatory')
if mibBuilder.loadTexts: nsVpnUsrDialupGrpIndex.setDescription('A unique value for schedule. Its value ranges between 0 and 65535 and may not be contiguous.')
nsVpnUsrDialupGrpName = MibTableColumn((1, 3, 6, 1, 4, 1, 3224, 4, 10, 1, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsVpnUsrDialupGrpName.setStatus('mandatory')
if mibBuilder.loadTexts: nsVpnUsrDialupGrpName.setDescription('dialup user group name.')
nsVpnUsrDialupGrpType = MibTableColumn((1, 3, 6, 1, 4, 1, 3224, 4, 10, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("undefined", 0), ("manual", 1), ("ike", 2), ("l2tp", 3), ("xauth", 4), ("auth", 5), ("external", 6)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsVpnUsrDialupGrpType.setStatus('mandatory')
if mibBuilder.loadTexts: nsVpnUsrDialupGrpType.setDescription('dial up group type.')
nsVpnUsrDialupGrpVsys = MibTableColumn((1, 3, 6, 1, 4, 1, 3224, 4, 10, 1, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsVpnUsrDialupGrpVsys.setStatus('mandatory')
if mibBuilder.loadTexts: nsVpnUsrDialupGrpVsys.setDescription('vsys this group belongs to.')
nsVpnManualKeyUsrTable = MibTable((1, 3, 6, 1, 4, 1, 3224, 4, 10, 2), )
if mibBuilder.loadTexts: nsVpnManualKeyUsrTable.setStatus('mandatory')
if mibBuilder.loadTexts: nsVpnManualKeyUsrTable.setDescription('This table specifies the configuration attributes for manual key user.')
nsVpnManualKeyUsrEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3224, 4, 10, 2, 1), ).setIndexNames((0, "NETSCREEN-USER-MIB", "nsVpnManualKeyUsrIndex"))
if mibBuilder.loadTexts: nsVpnManualKeyUsrEntry.setStatus('mandatory')
if mibBuilder.loadTexts: nsVpnManualKeyUsrEntry.setDescription('Each entry in the nsVpnManualkeyUsrTable holds a set of configuration parameters associated with an instance of manual key user.')
nsVpnManualKeyUsrIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 3224, 4, 10, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsVpnManualKeyUsrIndex.setStatus('mandatory')
if mibBuilder.loadTexts: nsVpnManualKeyUsrIndex.setDescription('A unique value for manual key user table. Its value ranges between 0 and 65535 and may not be contiguous.')
nsVpnManualKeyUsrName = MibTableColumn((1, 3, 6, 1, 4, 1, 3224, 4, 10, 2, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsVpnManualKeyUsrName.setStatus('mandatory')
if mibBuilder.loadTexts: nsVpnManualKeyUsrName.setDescription('User name.')
nsVpnManualKeyUsrGrp = MibTableColumn((1, 3, 6, 1, 4, 1, 3224, 4, 10, 2, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsVpnManualKeyUsrGrp.setStatus('mandatory')
if mibBuilder.loadTexts: nsVpnManualKeyUsrGrp.setDescription('group this user belongs to.')
nsVpnManualKeyUsrSILocal = MibTableColumn((1, 3, 6, 1, 4, 1, 3224, 4, 10, 2, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsVpnManualKeyUsrSILocal.setStatus('mandatory')
if mibBuilder.loadTexts: nsVpnManualKeyUsrSILocal.setDescription('Local Security Index')
nsVpnManualKeyUsrSIRemote = MibTableColumn((1, 3, 6, 1, 4, 1, 3224, 4, 10, 2, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsVpnManualKeyUsrSIRemote.setStatus('mandatory')
if mibBuilder.loadTexts: nsVpnManualKeyUsrSIRemote.setDescription('Remote Security Index')
nsVpnManualKeyUsrTunnelType = MibTableColumn((1, 3, 6, 1, 4, 1, 3224, 4, 10, 2, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("esp", 0), ("ah", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsVpnManualKeyUsrTunnelType.setStatus('mandatory')
if mibBuilder.loadTexts: nsVpnManualKeyUsrTunnelType.setDescription('vpn tunnel type.')
nsVpnManualKeyUsrEspEncAlg = MibTableColumn((1, 3, 6, 1, 4, 1, 3224, 4, 10, 2, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("null", 0), ("des-cbc", 1), ("triple-des-cbc", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsVpnManualKeyUsrEspEncAlg.setStatus('mandatory')
if mibBuilder.loadTexts: nsVpnManualKeyUsrEspEncAlg.setDescription('ESP Encryption Algorithm.')
nsVpnManualKeyUsrEspAuthAlg = MibTableColumn((1, 3, 6, 1, 4, 1, 3224, 4, 10, 2, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("null", 0), ("md5", 1), ("sha", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsVpnManualKeyUsrEspAuthAlg.setStatus('mandatory')
if mibBuilder.loadTexts: nsVpnManualKeyUsrEspAuthAlg.setDescription('ESP Authentication Algorithm.')
nsVpnManualKeyUsrAhHash = MibTableColumn((1, 3, 6, 1, 4, 1, 3224, 4, 10, 2, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("null", 0), ("md5", 1), ("sha", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsVpnManualKeyUsrAhHash.setStatus('mandatory')
if mibBuilder.loadTexts: nsVpnManualKeyUsrAhHash.setDescription('AH Hash Algorithm.')
nsVpnManualKeyUsrVsys = MibTableColumn((1, 3, 6, 1, 4, 1, 3224, 4, 10, 2, 1, 10), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsVpnManualKeyUsrVsys.setStatus('mandatory')
if mibBuilder.loadTexts: nsVpnManualKeyUsrVsys.setDescription('vsys this user belongs to.')
nsVpnAILUsrTable = MibTable((1, 3, 6, 1, 4, 1, 3224, 4, 10, 3), )
if mibBuilder.loadTexts: nsVpnAILUsrTable.setStatus('mandatory')
if mibBuilder.loadTexts: nsVpnAILUsrTable.setDescription('This table specifies the configuration attributes for AUTH/IKE/L2TP user.')
nsVpnAILUsrEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3224, 4, 10, 3, 1), ).setIndexNames((0, "NETSCREEN-USER-MIB", "nsVpnAILUsrIndex"))
if mibBuilder.loadTexts: nsVpnAILUsrEntry.setStatus('mandatory')
if mibBuilder.loadTexts: nsVpnAILUsrEntry.setDescription('Each entry in the nsVpnManualkeyUsrTable holds a set of configuration parameters associated with an instance of AUTH/IKE/L2TP user.')
nsVpnAILUsrIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 3224, 4, 10, 3, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsVpnAILUsrIndex.setStatus('mandatory')
if mibBuilder.loadTexts: nsVpnAILUsrIndex.setDescription('A unique value for Auth/Ike/l2tp user table. Its value ranges between 1 and 65535 and may not be contiguous.')
nsVpnAILUsrName = MibTableColumn((1, 3, 6, 1, 4, 1, 3224, 4, 10, 3, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsVpnAILUsrName.setStatus('mandatory')
if mibBuilder.loadTexts: nsVpnAILUsrName.setDescription('User name.')
nsVpnAILUsrGrp = MibTableColumn((1, 3, 6, 1, 4, 1, 3224, 4, 10, 3, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsVpnAILUsrGrp.setStatus('mandatory')
if mibBuilder.loadTexts: nsVpnAILUsrGrp.setDescription('group this user belongs to.')
nsVpnAILUsrStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 3224, 4, 10, 3, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disable", 0), ("enabled", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsVpnAILUsrStatus.setStatus('mandatory')
if mibBuilder.loadTexts: nsVpnAILUsrStatus.setDescription('User status')
nsVpnAILUsrIKE = MibTableColumn((1, 3, 6, 1, 4, 1, 3224, 4, 10, 3, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("no", 0), ("yes", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsVpnAILUsrIKE.setStatus('mandatory')
if mibBuilder.loadTexts: nsVpnAILUsrIKE.setDescription('Since Authentication, IKE L2TP can be combined together. This attribute is used to indicate if this user is an IKE user.')
nsVpnAILUsrIKEIdType = MibTableColumn((1, 3, 6, 1, 4, 1, 3224, 4, 10, 3, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10))).clone(namedValues=NamedValues(("not-set", 0), ("ipv4-addr", 1), ("fqdn", 2), ("usr-fqdn", 3), ("ipv4-addr-subnet", 4), ("ipv6-addr", 5), ("ipv6-addr-subnet", 6), ("ipv4-addr-addr-range", 7), ("ipv6-addr-addr-range", 8), ("der-asn1-dn", 9), ("der-asn1-gn", 10)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsVpnAILUsrIKEIdType.setStatus('mandatory')
if mibBuilder.loadTexts: nsVpnAILUsrIKEIdType.setDescription('IKE user type 1 means auto, other values are undefined.')
nsVpnAILUsrIKEId = MibTableColumn((1, 3, 6, 1, 4, 1, 3224, 4, 10, 3, 1, 7), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsVpnAILUsrIKEId.setStatus('mandatory')
if mibBuilder.loadTexts: nsVpnAILUsrIKEId.setDescription('IKE id.')
nsVpnAILUsrAuth = MibTableColumn((1, 3, 6, 1, 4, 1, 3224, 4, 10, 3, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("no", 0), ("yes", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsVpnAILUsrAuth.setStatus('mandatory')
if mibBuilder.loadTexts: nsVpnAILUsrAuth.setDescription('Since Authentication, IKE L2TP can be combined together. This attribute is used to indicate if this user is an Authentication user.')
nsVpnAILUsrL2TP = MibTableColumn((1, 3, 6, 1, 4, 1, 3224, 4, 10, 3, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("no", 0), ("yes", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsVpnAILUsrL2TP.setStatus('mandatory')
if mibBuilder.loadTexts: nsVpnAILUsrL2TP.setDescription('Since Authentication, IKE L2TP can be combined together. This attribute is used to indicate if this user is a L2TP user. The NetScreen-1000 does not support L2TP.')
nsVpnAILUsrL2tpRemoteIp = MibTableColumn((1, 3, 6, 1, 4, 1, 3224, 4, 10, 3, 1, 10), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsVpnAILUsrL2tpRemoteIp.setStatus('mandatory')
if mibBuilder.loadTexts: nsVpnAILUsrL2tpRemoteIp.setDescription('L2TP remote peer ip address.')
nsVpnAILUsrL2tpIpPool = MibTableColumn((1, 3, 6, 1, 4, 1, 3224, 4, 10, 3, 1, 11), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsVpnAILUsrL2tpIpPool.setStatus('mandatory')
if mibBuilder.loadTexts: nsVpnAILUsrL2tpIpPool.setDescription('ip pool entity name.')
nsVpnAILUsrL2tpIp = MibTableColumn((1, 3, 6, 1, 4, 1, 3224, 4, 10, 3, 1, 12), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsVpnAILUsrL2tpIp.setStatus('mandatory')
if mibBuilder.loadTexts: nsVpnAILUsrL2tpIp.setDescription('L2TP local ip address.')
nsVpnAILUsrL2tpPriDnsIp = MibTableColumn((1, 3, 6, 1, 4, 1, 3224, 4, 10, 3, 1, 13), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsVpnAILUsrL2tpPriDnsIp.setStatus('mandatory')
if mibBuilder.loadTexts: nsVpnAILUsrL2tpPriDnsIp.setDescription('primary DNS server IP address for L2TP user.')
nsVpnAILUsrL2tpSecDnsIp = MibTableColumn((1, 3, 6, 1, 4, 1, 3224, 4, 10, 3, 1, 14), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsVpnAILUsrL2tpSecDnsIp.setStatus('mandatory')
if mibBuilder.loadTexts: nsVpnAILUsrL2tpSecDnsIp.setDescription('secondary DNS server IP address for L2TP user.')
nsVpnAILUsrL2tpPriWinsIp = MibTableColumn((1, 3, 6, 1, 4, 1, 3224, 4, 10, 3, 1, 15), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsVpnAILUsrL2tpPriWinsIp.setStatus('mandatory')
if mibBuilder.loadTexts: nsVpnAILUsrL2tpPriWinsIp.setDescription('primary WINS server IP address for L2TP user.')
nsVpnAILUsrL2tpSecWinsIp = MibTableColumn((1, 3, 6, 1, 4, 1, 3224, 4, 10, 3, 1, 16), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsVpnAILUsrL2tpSecWinsIp.setStatus('mandatory')
if mibBuilder.loadTexts: nsVpnAILUsrL2tpSecWinsIp.setDescription('secondary WINS server IP address for L2TP user.')
nsVpnAILUsrVsys = MibTableColumn((1, 3, 6, 1, 4, 1, 3224, 4, 10, 3, 1, 17), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsVpnAILUsrVsys.setStatus('mandatory')
if mibBuilder.loadTexts: nsVpnAILUsrVsys.setDescription('vsys this user belongs to.')
mibBuilder.exportSymbols("NETSCREEN-USER-MIB", nsVpnUsrDialupGrpName=nsVpnUsrDialupGrpName, nsVpnAILUsrGrp=nsVpnAILUsrGrp, nsVpnAILUsrL2tpSecWinsIp=nsVpnAILUsrL2tpSecWinsIp, nsVpnManualKeyUsrAhHash=nsVpnManualKeyUsrAhHash, nsVpnAILUsrIKE=nsVpnAILUsrIKE, nsVpnUsrDialupGrpIndex=nsVpnUsrDialupGrpIndex, nsVpnAILUsrL2TP=nsVpnAILUsrL2TP, nsVpnManualKeyUsrSILocal=nsVpnManualKeyUsrSILocal, nsVpnAILUsrL2tpPriDnsIp=nsVpnAILUsrL2tpPriDnsIp, nsVpnAILUsrL2tpPriWinsIp=nsVpnAILUsrL2tpPriWinsIp, nsVpnManualKeyUsrSIRemote=nsVpnManualKeyUsrSIRemote, nsVpnAILUsrL2tpIp=nsVpnAILUsrL2tpIp, nsVpnUsrDialupGrpEntry=nsVpnUsrDialupGrpEntry, nsVpnManualKeyUsrEspAuthAlg=nsVpnManualKeyUsrEspAuthAlg, nsVpnUsrDialupGrpVsys=nsVpnUsrDialupGrpVsys, nsVpnAILUsrTable=nsVpnAILUsrTable, nsVpnManualKeyUsrVsys=nsVpnManualKeyUsrVsys, nsVpnAILUsrStatus=nsVpnAILUsrStatus, nsVpnAILUsrL2tpRemoteIp=nsVpnAILUsrL2tpRemoteIp, nsVpnUsrDialupGrpType=nsVpnUsrDialupGrpType, nsVpnManualKeyUsrEntry=nsVpnManualKeyUsrEntry, nsVpnManualKeyUsrName=nsVpnManualKeyUsrName, nsVpnAILUsrIKEId=nsVpnAILUsrIKEId, nsVpnUsrDialupGrpTable=nsVpnUsrDialupGrpTable, nsVpnAILUsrEntry=nsVpnAILUsrEntry, nsVpnAILUsrL2tpSecDnsIp=nsVpnAILUsrL2tpSecDnsIp, nsVpnManualKeyUsrGrp=nsVpnManualKeyUsrGrp, nsVpnAILUsrIndex=nsVpnAILUsrIndex, nsVpnAILUsrAuth=nsVpnAILUsrAuth, nsVpnManualKeyUsrTable=nsVpnManualKeyUsrTable, nsVpnAILUsrL2tpIpPool=nsVpnAILUsrL2tpIpPool, nsVpnManualKeyUsrIndex=nsVpnManualKeyUsrIndex, nsVpnManualKeyUsrTunnelType=nsVpnManualKeyUsrTunnelType, nsVpnAILUsrVsys=nsVpnAILUsrVsys, nsVpnManualKeyUsrEspEncAlg=nsVpnManualKeyUsrEspEncAlg, nsVpnUser=nsVpnUser, nsVpnAILUsrIKEIdType=nsVpnAILUsrIKEIdType, nsVpnAILUsrName=nsVpnAILUsrName)
