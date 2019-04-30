#
# PySNMP MIB module OPTIX-OID-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/OPTIX-OID-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:26:01 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
iso, NotificationType, Unsigned32, enterprises, Counter32, MibIdentifier, ModuleIdentity, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, Gauge32, ObjectIdentity, TimeTicks, Integer32, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "NotificationType", "Unsigned32", "enterprises", "Counter32", "MibIdentifier", "ModuleIdentity", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "Gauge32", "ObjectIdentity", "TimeTicks", "Integer32", "Counter64")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
huawei = MibIdentifier((1, 3, 6, 1, 4, 1, 2011))
products = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2))
transmission = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 25))
optixCommon = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 25, 3))
optixCommonSdh = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 10))
optixCommonSonet = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20))
optixProvision = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 25, 4))
optixProvisionSdh = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 10))
optixProvisionSonet = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 20))
mibBuilder.exportSymbols("OPTIX-OID-MIB", optixCommonSonet=optixCommonSonet, transmission=transmission, optixCommon=optixCommon, optixProvision=optixProvision, optixProvisionSonet=optixProvisionSonet, optixCommonSdh=optixCommonSdh, optixProvisionSdh=optixProvisionSdh, products=products, huawei=huawei)
