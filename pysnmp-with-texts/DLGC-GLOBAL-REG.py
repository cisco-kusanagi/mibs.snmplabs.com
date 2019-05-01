#
# PySNMP MIB module DLGC-GLOBAL-REG (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/DLGC-GLOBAL-REG
# Produced by pysmi-0.3.4 at Wed May  1 12:47:44 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Gauge32, Unsigned32, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, IpAddress, Counter32, Integer32, enterprises, TimeTicks, ObjectIdentity, Bits, iso, ModuleIdentity, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "Unsigned32", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "IpAddress", "Counter32", "Integer32", "enterprises", "TimeTicks", "ObjectIdentity", "Bits", "iso", "ModuleIdentity", "NotificationType")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
dialogic = MibIdentifier((1, 3, 6, 1, 4, 1, 3028))
dlgPlatform = MibIdentifier((1, 3, 6, 1, 4, 1, 3028, 1))
dlgResources = MibIdentifier((1, 3, 6, 1, 4, 1, 3028, 2))
dlgNetworkInterfaces = MibIdentifier((1, 3, 6, 1, 4, 1, 3028, 3))
dlgServiceProviders = MibIdentifier((1, 3, 6, 1, 4, 1, 3028, 4))
dlgApplications = MibIdentifier((1, 3, 6, 1, 4, 1, 3028, 5))
dlgProducts = MibIdentifier((1, 3, 6, 1, 4, 1, 3028, 6))
dlgHardwareInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 3028, 1, 1))
dlgPerformanceInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 3028, 1, 2))
dlgR4Resources = MibIdentifier((1, 3, 6, 1, 4, 1, 3028, 2, 1))
dlgDM3Resources = MibIdentifier((1, 3, 6, 1, 4, 1, 3028, 2, 2))
dlgTransmissions = MibIdentifier((1, 3, 6, 1, 4, 1, 3028, 3, 1))
dlgTapi = MibIdentifier((1, 3, 6, 1, 4, 1, 3028, 4, 1))
mibBuilder.exportSymbols("DLGC-GLOBAL-REG", dlgHardwareInfo=dlgHardwareInfo, dlgPlatform=dlgPlatform, dlgProducts=dlgProducts, dlgR4Resources=dlgR4Resources, dlgServiceProviders=dlgServiceProviders, dlgResources=dlgResources, dlgPerformanceInfo=dlgPerformanceInfo, dlgDM3Resources=dlgDM3Resources, dlgNetworkInterfaces=dlgNetworkInterfaces, dlgTransmissions=dlgTransmissions, dlgTapi=dlgTapi, dialogic=dialogic, dlgApplications=dlgApplications)
