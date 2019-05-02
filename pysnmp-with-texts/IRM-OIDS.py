#
# PySNMP MIB module IRM-OIDS (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/IRM-OIDS
# Produced by pysmi-0.3.4 at Wed May  1 11:44:24 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint")
cabletron, = mibBuilder.importSymbols("CTRON-OIDS", "cabletron")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, TimeTicks, Counter32, Integer32, Counter64, NotificationType, ObjectIdentity, iso, MibIdentifier, ModuleIdentity, Unsigned32, Bits, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "TimeTicks", "Counter32", "Integer32", "Counter64", "NotificationType", "ObjectIdentity", "iso", "MibIdentifier", "ModuleIdentity", "Unsigned32", "Bits", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
commsDevice = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 1))
layerMgmt = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 2))
common = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 1, 1))
repeater = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 1, 2))
bridge = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 1, 3))
router = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 1, 4))
product = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 1, 5))
subsystem = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 1, 6))
commonRev1 = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 1, 1, 1))
sysOIDs = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 1, 1, 2))
repeaterRev1 = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 1, 2, 1))
repeaterRev2 = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 1, 2, 2))
subSysMMAC = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 1, 6, 1))
subSysDevice = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 1, 6, 2))
ups = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 1, 6, 3))
dl = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 1, 6, 4))
backplaneProtocol = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 1, 6, 5))
nb30Rev1 = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 1, 6, 12))
sysOtherType = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 1, 1, 2, 1))
sysChassis = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 1, 1, 2, 2))
sysRepeaters = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 1, 1, 2, 3))
sysBridges = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 1, 1, 2, 4))
sysRouters = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 1, 1, 2, 5))
sysIntDev = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 1, 1, 2, 6))
mibBuilder.exportSymbols("IRM-OIDS", bridge=bridge, product=product, sysIntDev=sysIntDev, subSysDevice=subSysDevice, subsystem=subsystem, commonRev1=commonRev1, router=router, sysRepeaters=sysRepeaters, dl=dl, sysOIDs=sysOIDs, backplaneProtocol=backplaneProtocol, sysChassis=sysChassis, repeaterRev1=repeaterRev1, sysOtherType=sysOtherType, commsDevice=commsDevice, common=common, repeater=repeater, subSysMMAC=subSysMMAC, ups=ups, nb30Rev1=nb30Rev1, sysBridges=sysBridges, layerMgmt=layerMgmt, sysRouters=sysRouters, repeaterRev2=repeaterRev2)
