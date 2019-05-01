#
# PySNMP MIB module DATACOM-SMI (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/DATACOM-SMI
# Produced by pysmi-0.3.4 at Wed May  1 12:36:57 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Bits, NotificationType, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, enterprises, iso, Counter32, Counter64, ModuleIdentity, IpAddress, Integer32, Gauge32, Unsigned32, ObjectIdentity, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "NotificationType", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "enterprises", "iso", "Counter32", "Counter64", "ModuleIdentity", "IpAddress", "Integer32", "Gauge32", "Unsigned32", "ObjectIdentity", "MibIdentifier")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("DATACOM-SMI", datacomModules=datacomModules, datacomAccessDevices=datacomAccessDevices, datacomModemsMIBs=datacomModemsMIBs, datacomExpGenericMIBs=datacomExpGenericMIBs, datacomModems=datacomModems, datacom=datacom, datacomExpModemsMIBs=datacomExpModemsMIBs, datacomManagementCards=datacomManagementCards, datacomRegistrations=datacomRegistrations, datacomAccessDevicesMIBs=datacomAccessDevicesMIBs, datacomExpAccessDevicesMIBs=datacomExpAccessDevicesMIBs, datacomProductsMIBs=datacomProductsMIBs, datacomGenericMIBs=datacomGenericMIBs, datacomExperimental=datacomExperimental, datacomExpProductsMIBs=datacomExpProductsMIBs)
