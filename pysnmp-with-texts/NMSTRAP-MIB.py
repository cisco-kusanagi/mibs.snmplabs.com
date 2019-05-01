#
# PySNMP MIB module NMSTRAP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/NMSTRAP-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:22:32 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint")
ifIndex, ifType, ifDescr = mibBuilder.importSymbols("IF-MIB", "ifIndex", "ifType", "ifDescr")
adslPtOutSpeed, adslPtInSpeed, adslPtOutDrop, adslPtStatus, adslLineUser, adslMemLoad, adslPtOutPkts, adslPtOutError, adslPtInError, adslPtInDrop, adslPtInCRC, adslProductID, adslPtSpeed, adslPtInPkts, adslConfigAddr, adslCPULoad = mibBuilder.importSymbols("NMS-1705", "adslPtOutSpeed", "adslPtInSpeed", "adslPtOutDrop", "adslPtStatus", "adslLineUser", "adslMemLoad", "adslPtOutPkts", "adslPtOutError", "adslPtInError", "adslPtInDrop", "adslPtInCRC", "adslProductID", "adslPtSpeed", "adslPtInPkts", "adslConfigAddr", "adslCPULoad")
nms, = mibBuilder.importSymbols("NMS-SMI", "nms")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
sysUpTime, = mibBuilder.importSymbols("SNMPv2-MIB", "sysUpTime")
IpAddress, Counter32, Bits, iso, NotificationType, ModuleIdentity, Unsigned32, MibIdentifier, ObjectIdentity, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, NotificationType, TimeTicks, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "Counter32", "Bits", "iso", "NotificationType", "ModuleIdentity", "Unsigned32", "MibIdentifier", "ObjectIdentity", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "NotificationType", "TimeTicks", "Counter64")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
adslConnection = NotificationType((1, 3, 6, 1, 4, 1, 11606, 10) + (0,0)).setObjects(("NMS-1705", "adslLineUser"), ("NMS-1705", "adslProductID"), ("NMS-1705", "adslConfigAddr"))
if mibBuilder.loadTexts: adslConnection.setDescription('A line trap signifies that a line connection has been established')
adslPeriod = NotificationType((1, 3, 6, 1, 4, 1, 11606, 10) + (0,1)).setObjects(("NMS-1705", "adslMemLoad"), ("NMS-1705", "adslCPULoad"), ("NMS-1705", "adslPtInCRC"), ("NMS-1705", "adslPtStatus"), ("NMS-1705", "adslPtSpeed"), ("NMS-1705", "adslPtOutPkts"), ("NMS-1705", "adslPtInPkts"), ("NMS-1705", "adslPtOutError"), ("NMS-1705", "adslPtInError"), ("NMS-1705", "adslPtOutSpeed"), ("NMS-1705", "adslPtInSpeed"), ("NMS-1705", "adslPtOutDrop"), ("NMS-1705", "adslPtInDrop"))
if mibBuilder.loadTexts: adslPeriod.setDescription('A adsl period trap signifies the current information of online connect port.')
mibBuilder.exportSymbols("NMSTRAP-MIB", adslPeriod=adslPeriod, adslConnection=adslConnection)
