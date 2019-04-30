#
# PySNMP MIB module NMSTRAP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/NMSTRAP-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:12:49 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint")
ifIndex, ifType, ifDescr = mibBuilder.importSymbols("IF-MIB", "ifIndex", "ifType", "ifDescr")
adslCPULoad, adslPtOutSpeed, adslPtOutError, adslPtOutDrop, adslPtStatus, adslPtSpeed, adslPtInPkts, adslPtInError, adslPtInDrop, adslConfigAddr, adslMemLoad, adslProductID, adslPtOutPkts, adslPtInSpeed, adslPtInCRC, adslLineUser = mibBuilder.importSymbols("NMS-1705", "adslCPULoad", "adslPtOutSpeed", "adslPtOutError", "adslPtOutDrop", "adslPtStatus", "adslPtSpeed", "adslPtInPkts", "adslPtInError", "adslPtInDrop", "adslConfigAddr", "adslMemLoad", "adslProductID", "adslPtOutPkts", "adslPtInSpeed", "adslPtInCRC", "adslLineUser")
nms, = mibBuilder.importSymbols("NMS-SMI", "nms")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
sysUpTime, = mibBuilder.importSymbols("SNMPv2-MIB", "sysUpTime")
NotificationType, IpAddress, TimeTicks, Counter64, Gauge32, Integer32, iso, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, Unsigned32, MibIdentifier, Counter32, Bits, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "IpAddress", "TimeTicks", "Counter64", "Gauge32", "Integer32", "iso", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "Unsigned32", "MibIdentifier", "Counter32", "Bits", "NotificationType")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
adslConnection = NotificationType((1, 3, 6, 1, 4, 1, 11606, 10) + (0,0)).setObjects(("NMS-1705", "adslLineUser"), ("NMS-1705", "adslProductID"), ("NMS-1705", "adslConfigAddr"))
adslPeriod = NotificationType((1, 3, 6, 1, 4, 1, 11606, 10) + (0,1)).setObjects(("NMS-1705", "adslMemLoad"), ("NMS-1705", "adslCPULoad"), ("NMS-1705", "adslPtInCRC"), ("NMS-1705", "adslPtStatus"), ("NMS-1705", "adslPtSpeed"), ("NMS-1705", "adslPtOutPkts"), ("NMS-1705", "adslPtInPkts"), ("NMS-1705", "adslPtOutError"), ("NMS-1705", "adslPtInError"), ("NMS-1705", "adslPtOutSpeed"), ("NMS-1705", "adslPtInSpeed"), ("NMS-1705", "adslPtOutDrop"), ("NMS-1705", "adslPtInDrop"))
mibBuilder.exportSymbols("NMSTRAP-MIB", adslPeriod=adslPeriod, adslConnection=adslConnection)
