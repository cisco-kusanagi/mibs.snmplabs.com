#
# PySNMP MIB module DLGC-GLOBAL-REG (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/DLGC-GLOBAL-REG
# Produced by pysmi-0.3.4 at Mon Apr 29 18:32:45 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Gauge32, Counter32, iso, MibIdentifier, Integer32, ModuleIdentity, ObjectIdentity, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Counter64, IpAddress, enterprises, Bits, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "Counter32", "iso", "MibIdentifier", "Integer32", "ModuleIdentity", "ObjectIdentity", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Counter64", "IpAddress", "enterprises", "Bits", "Unsigned32")
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
mibBuilder.exportSymbols("DLGC-GLOBAL-REG", dlgTransmissions=dlgTransmissions, dlgDM3Resources=dlgDM3Resources, dlgNetworkInterfaces=dlgNetworkInterfaces, dlgPlatform=dlgPlatform, dlgPerformanceInfo=dlgPerformanceInfo, dlgR4Resources=dlgR4Resources, dlgProducts=dlgProducts, dlgApplications=dlgApplications, dlgResources=dlgResources, dlgTapi=dlgTapi, dialogic=dialogic, dlgHardwareInfo=dlgHardwareInfo, dlgServiceProviders=dlgServiceProviders)
