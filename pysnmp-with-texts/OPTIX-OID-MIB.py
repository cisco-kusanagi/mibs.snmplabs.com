#
# PySNMP MIB module OPTIX-OID-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/OPTIX-OID-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:35:13 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
enterprises, Bits, ModuleIdentity, IpAddress, Gauge32, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Counter32, ObjectIdentity, MibIdentifier, Integer32, Unsigned32, iso, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "enterprises", "Bits", "ModuleIdentity", "IpAddress", "Gauge32", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Counter32", "ObjectIdentity", "MibIdentifier", "Integer32", "Unsigned32", "iso", "NotificationType")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
huawei = MibIdentifier((1, 3, 6, 1, 4, 1, 2011))
products = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2))
transmission = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 25))
optixCommon = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 25, 3))
optixCommonSdh = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 10))
optixCommonSonet = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20))
optixProvision = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 25, 4))
optixProvisionSdh = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 10))
optixProvisionSonet = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 20))
mibBuilder.exportSymbols("OPTIX-OID-MIB", optixCommonSonet=optixCommonSonet, optixProvisionSdh=optixProvisionSdh, optixCommon=optixCommon, transmission=transmission, huawei=huawei, optixCommonSdh=optixCommonSdh, products=products, optixProvisionSonet=optixProvisionSonet, optixProvision=optixProvision)
