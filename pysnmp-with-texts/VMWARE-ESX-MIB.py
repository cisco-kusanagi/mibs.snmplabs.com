#
# PySNMP MIB module VMWARE-ESX-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/VMWARE-ESX-MIB
# Produced by pysmi-0.3.4 at Wed May  1 15:34:51 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Counter32, ObjectIdentity, Unsigned32, NotificationType, TimeTicks, MibIdentifier, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ModuleIdentity, Bits, iso, Counter64, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "ObjectIdentity", "Unsigned32", "NotificationType", "TimeTicks", "MibIdentifier", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ModuleIdentity", "Bits", "iso", "Counter64", "Integer32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
vmwOID, vmwProductSpecific = mibBuilder.importSymbols("VMWARE-ROOT-MIB", "vmwOID", "vmwProductSpecific")
oidESX = MibIdentifier((1, 3, 6, 1, 4, 1, 6876, 60, 1))
vmwESX = MibIdentifier((1, 3, 6, 1, 4, 1, 6876, 4, 1))
esxVMKernel = MibIdentifier((1, 3, 6, 1, 4, 1, 6876, 4, 1, 1))
vmkLoaded = MibScalar((1, 3, 6, 1, 4, 1, 6876, 4, 1, 1, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vmkLoaded.setStatus('mandatory')
if mibBuilder.loadTexts: vmkLoaded.setDescription('Has the vmkernel been loaded? (yes/no)')
mibBuilder.exportSymbols("VMWARE-ESX-MIB", vmwESX=vmwESX, esxVMKernel=esxVMKernel, vmkLoaded=vmkLoaded, oidESX=oidESX)
