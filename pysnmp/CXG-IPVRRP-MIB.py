#
# PySNMP MIB module CXG-IPVRRP-MIB (http://pysnmp.sf.net)
# Produced by pysmi-0.0.1 from CXG-IPVRRP-MIB at Mon May  4 01:11:03 2015
# On host cray platform Linux version 2.6.37.6-smp by user tt
# Using Python version 2.7.2 (default, Apr  2 2012, 20:32:47) 
#
( Integer, ObjectIdentifier, OctetString, ) = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
( NamedValues, ) = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
( ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, ) = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint")
( cxCfgIp, ) = mibBuilder.importSymbols("CXProduct-SMI", "cxCfgIp")
( Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, TimeTicks, iso, Gauge32, MibIdentifier, Bits, Counter32, ) = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "TimeTicks", "iso", "Gauge32", "MibIdentifier", "Bits", "Counter32")
cxVrrpTable = MibTable(cxCfgIp.getName() + (5,), )
cxVrrpEntry = MibTableRow(cxVrrpTable.getName() + (1,), ).setIndexNames((0, "CXG-IPVRRP-MIB", "cxVrrpIPPort"), (0, "CXG-IPVRRP-MIB", "cxVrrpVrID"))
cxVrrpIPPort = MibTableColumn(cxVrrpEntry.getName() + (1,), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1,255))).setMaxAccess("readonly")
cxVrrpVrID = MibTableColumn(cxVrrpEntry.getName() + (2,), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1,255))).setMaxAccess("readonly")
cxVrrpPriority = MibTableColumn(cxVrrpEntry.getName() + (3,), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1,255)).clone(100)).setMaxAccess("readwrite")
cxVrrpIPAddress = MibTableColumn(cxVrrpEntry.getName() + (4,), IpAddress()).setMaxAccess("readwrite")
cxVrrpAdvertiseInterval = MibTableColumn(cxVrrpEntry.getName() + (5,), Integer32().subtype(subtypeSpec=ValueRangeConstraint(100,65335)).clone(1000)).setMaxAccess("readwrite")
cxVrrpPreemptiveMode = MibTableColumn(cxVrrpEntry.getName() + (6,), Integer32().subtype(subtypeSpec=SingleValueConstraint(1, 2,)).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2),)).clone('enabled')).setMaxAccess("readwrite")
cxVrrpRowStatus = MibTableColumn(cxVrrpEntry.getName() + (10,), Integer32().subtype(subtypeSpec=SingleValueConstraint(1, 2,)).clone(namedValues=NamedValues(("invalid", 1), ("valid", 2),))).setMaxAccess("readwrite")
mibBuilder.exportSymbols("CXG-IPVRRP-MIB", cxVrrpTable=cxVrrpTable, cxVrrpVrID=cxVrrpVrID, cxVrrpPriority=cxVrrpPriority, cxVrrpIPAddress=cxVrrpIPAddress, cxVrrpPreemptiveMode=cxVrrpPreemptiveMode, cxVrrpRowStatus=cxVrrpRowStatus, cxVrrpEntry=cxVrrpEntry, cxVrrpIPPort=cxVrrpIPPort, cxVrrpAdvertiseInterval=cxVrrpAdvertiseInterval)
