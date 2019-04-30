#
# PySNMP MIB module DATACOM-SMI (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/DATACOM-SMI
# Produced by pysmi-0.3.4 at Mon Apr 29 18:21:32 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, enterprises, Counter32, ModuleIdentity, Unsigned32, NotificationType, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, Counter64, ObjectIdentity, Integer32, Bits, TimeTicks, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "enterprises", "Counter32", "ModuleIdentity", "Unsigned32", "NotificationType", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "Counter64", "ObjectIdentity", "Integer32", "Bits", "TimeTicks", "Gauge32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
datacom = MibIdentifier((1, 3, 6, 1, 4, 1, 3709))
datacomRegistrations = MibIdentifier((1, 3, 6, 1, 4, 1, 3709, 1))
datacomGenericMIBs = MibIdentifier((1, 3, 6, 1, 4, 1, 3709, 2))
datacomProductsMIBs = MibIdentifier((1, 3, 6, 1, 4, 1, 3709, 3))
datacomExperimental = MibIdentifier((1, 3, 6, 1, 4, 1, 3709, 4))
datacomModules = MibIdentifier((1, 3, 6, 1, 4, 1, 3709, 1, 1))
datacomManagementCards = MibIdentifier((1, 3, 6, 1, 4, 1, 3709, 1, 2))
datacomModems = MibIdentifier((1, 3, 6, 1, 4, 1, 3709, 1, 3))
datacomAccessDevices = MibIdentifier((1, 3, 6, 1, 4, 1, 3709, 1, 5))
datacomModemsMIBs = MibIdentifier((1, 3, 6, 1, 4, 1, 3709, 3, 3))
datacomAccessDevicesMIBs = MibIdentifier((1, 3, 6, 1, 4, 1, 3709, 3, 5))
datacomExpGenericMIBs = MibIdentifier((1, 3, 6, 1, 4, 1, 3709, 4, 2))
datacomExpProductsMIBs = MibIdentifier((1, 3, 6, 1, 4, 1, 3709, 4, 3))
datacomExpModemsMIBs = MibIdentifier((1, 3, 6, 1, 4, 1, 3709, 4, 3, 3))
datacomExpAccessDevicesMIBs = MibIdentifier((1, 3, 6, 1, 4, 1, 3709, 4, 3, 5))
mibBuilder.exportSymbols("DATACOM-SMI", datacomExperimental=datacomExperimental, datacomRegistrations=datacomRegistrations, datacomAccessDevices=datacomAccessDevices, datacom=datacom, datacomModems=datacomModems, datacomExpProductsMIBs=datacomExpProductsMIBs, datacomModemsMIBs=datacomModemsMIBs, datacomProductsMIBs=datacomProductsMIBs, datacomExpGenericMIBs=datacomExpGenericMIBs, datacomGenericMIBs=datacomGenericMIBs, datacomModules=datacomModules, datacomExpAccessDevicesMIBs=datacomExpAccessDevicesMIBs, datacomManagementCards=datacomManagementCards, datacomAccessDevicesMIBs=datacomAccessDevicesMIBs, datacomExpModemsMIBs=datacomExpModemsMIBs)
