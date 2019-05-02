#
# PySNMP MIB module TPT-PORT-CONFIG-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/TPT-PORT-CONFIG-MIB
# Produced by pysmi-0.3.4 at Wed May  1 15:26:19 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Unsigned32, Bits, ObjectIdentity, Integer32, Counter32, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, Gauge32, ModuleIdentity, iso, IpAddress, TimeTicks, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "Bits", "ObjectIdentity", "Integer32", "Counter32", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "Gauge32", "ModuleIdentity", "iso", "IpAddress", "TimeTicks", "MibIdentifier")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
tpt_tpa_objs, = mibBuilder.importSymbols("TPT-TPAMIBS-MIB", "tpt-tpa-objs")
tpt_port_config_objs = ModuleIdentity((1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 4)).setLabel("tpt-port-config-objs")
tpt_port_config_objs.setRevisions(('2016-05-25 18:54',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: tpt_port_config_objs.setRevisionsDescriptions(('Updated copyright information. Minor MIB syntax fixes.',))
if mibBuilder.loadTexts: tpt_port_config_objs.setLastUpdated('201605251854Z')
if mibBuilder.loadTexts: tpt_port_config_objs.setOrganization('Trend Micro, Inc.')
if mibBuilder.loadTexts: tpt_port_config_objs.setContactInfo('www.trendmicro.com')
if mibBuilder.loadTexts: tpt_port_config_objs.setDescription("Configurable items of an interface port on the device. Copyright (C) 2016 Trend Micro Incorporated. All Rights Reserved. Trend Micro makes no warranty of any kind with regard to this material, including, but not limited to, the implied warranties of merchantability and fitness for a particular purpose. Trend Micro shall not be liable for errors contained herein or for incidental or consequential damages in connection with the furnishing, performance, or use of this material. This document contains proprietary information, which is protected by copyright. No part of this document may be photocopied, reproduced, or translated into another language without the prior written consent of Trend Micro. The information is provided 'as is' without warranty of any kind and is subject to change without notice. The only warranties for Trend Micro products and services are set forth in the express warranty statements accompanying such products and services. Nothing herein should be construed as constituting an additional warranty. Trend Micro shall not be liable for technical or editorial errors or omissions contained herein. TippingPoint(R), the TippingPoint logo, and Digital Vaccine(R) are registered trademarks of Trend Micro. All other company and product names may be trademarks of their respective holders. All rights reserved. This document contains confidential information, trade secrets or both, which are the property of Trend Micro. No part of this documentation may be reproduced in any form or by any means or used to make any derivative work (such as translation, transformation, or adaptation) without written permission from Trend Micro or one of its subsidiaries. All other company and product names may be trademarks of their respective holders. ")
class LineSpeed(TextualConvention, Integer32):
    description = 'An indication of configured network line speed.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5))
    namedValues = NamedValues(("default", 0), ("gigabit", 1), ("hundred-megabit", 2), ("ten-megabit", 3), ("ten-gigabit", 4), ("fourty-gigabit", 5))

class DuplexSetting(TextualConvention, Integer32):
    description = 'An indication of configured duplex mode.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("default", 0), ("half", 1), ("full", 2))

class AutoNegotiation(TextualConvention, Integer32):
    description = 'An indication of configured auto-negotiation mode.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("default", 0), ("on", 1), ("off", 2))

class EnabledOrNot(TextualConvention, Integer32):
    description = 'An indication of whether a feature is configured as enabled or disabled.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("disabled", 0), ("enabled", 1))

class FailoverAction(TextualConvention, Integer32):
    description = 'An indication of whether a segment should pass traffic on failover.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("block", 0), ("permit", 1))

class LinkDownMode(TextualConvention, Integer32):
    description = 'An indication of configured link-down-synchronization mode.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("hub", 0), ("breaker", 1), ("wire", 2))

portConfigTable = MibTable((1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 4, 1), )
if mibBuilder.loadTexts: portConfigTable.setStatus('current')
if mibBuilder.loadTexts: portConfigTable.setDescription('Table of slots/ports on the device and their configuration settings.')
portConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 4, 1, 1), ).setIndexNames((0, "TPT-PORT-CONFIG-MIB", "portConfigSlot"), (0, "TPT-PORT-CONFIG-MIB", "portConfigPort"))
if mibBuilder.loadTexts: portConfigEntry.setStatus('current')
if mibBuilder.loadTexts: portConfigEntry.setDescription('An entry in the slot/port table. Rows cannot be created or deleted.')
portConfigSlot = MibTableColumn((1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 4, 1, 1, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: portConfigSlot.setStatus('current')
if mibBuilder.loadTexts: portConfigSlot.setDescription('Slot number for this port.')
portConfigPort = MibTableColumn((1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 4, 1, 1, 2), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: portConfigPort.setStatus('current')
if mibBuilder.loadTexts: portConfigPort.setDescription('Port number for this port.')
portConfigLineSpeed = MibTableColumn((1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 4, 1, 1, 3), LineSpeed()).setMaxAccess("readonly")
if mibBuilder.loadTexts: portConfigLineSpeed.setStatus('current')
if mibBuilder.loadTexts: portConfigLineSpeed.setDescription('The line speed configuration setting of this port.')
portConfigDuplex = MibTableColumn((1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 4, 1, 1, 4), DuplexSetting()).setMaxAccess("readonly")
if mibBuilder.loadTexts: portConfigDuplex.setStatus('current')
if mibBuilder.loadTexts: portConfigDuplex.setDescription('The duplex configuration setting of this port.')
portConfigAutoNeg = MibTableColumn((1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 4, 1, 1, 5), AutoNegotiation()).setMaxAccess("readonly")
if mibBuilder.loadTexts: portConfigAutoNeg.setStatus('current')
if mibBuilder.loadTexts: portConfigAutoNeg.setDescription('The auto-negotiation configuration setting of this port.')
portConfigShutdown = MibTableColumn((1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 4, 1, 1, 6), EnabledOrNot()).setMaxAccess("readonly")
if mibBuilder.loadTexts: portConfigShutdown.setStatus('current')
if mibBuilder.loadTexts: portConfigShutdown.setDescription('The shutdown configuration setting of this port. Shutdown enabled means that the port is manually removed from service. Shutdown disabled means that the port is free to come up normally.')
portConfigLoopback = MibTableColumn((1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 4, 1, 1, 7), EnabledOrNot()).setMaxAccess("readonly")
if mibBuilder.loadTexts: portConfigLoopback.setStatus('current')
if mibBuilder.loadTexts: portConfigLoopback.setDescription('The loopback (on or off) configuration setting of this port.')
portConfigFailover = MibTableColumn((1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 4, 1, 1, 8), FailoverAction()).setMaxAccess("readonly")
if mibBuilder.loadTexts: portConfigFailover.setStatus('current')
if mibBuilder.loadTexts: portConfigFailover.setDescription('The failover action (block or permit) configuration setting of this port.')
portConfigLDSMode = MibTableColumn((1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 4, 1, 1, 9), LinkDownMode()).setMaxAccess("readonly")
if mibBuilder.loadTexts: portConfigLDSMode.setStatus('current')
if mibBuilder.loadTexts: portConfigLDSMode.setDescription('The link-down sync mode (hub, breaker, or wire) setting of this port.')
portConfigLDSTimeout = MibTableColumn((1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 4, 1, 1, 10), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: portConfigLDSTimeout.setStatus('current')
if mibBuilder.loadTexts: portConfigLDSTimeout.setDescription('The link-down sync timeout configuration setting of this port.')
mibBuilder.exportSymbols("TPT-PORT-CONFIG-MIB", portConfigLineSpeed=portConfigLineSpeed, portConfigShutdown=portConfigShutdown, AutoNegotiation=AutoNegotiation, EnabledOrNot=EnabledOrNot, portConfigLoopback=portConfigLoopback, DuplexSetting=DuplexSetting, LineSpeed=LineSpeed, portConfigTable=portConfigTable, portConfigPort=portConfigPort, portConfigLDSTimeout=portConfigLDSTimeout, portConfigDuplex=portConfigDuplex, portConfigSlot=portConfigSlot, tpt_port_config_objs=tpt_port_config_objs, portConfigLDSMode=portConfigLDSMode, LinkDownMode=LinkDownMode, portConfigAutoNeg=portConfigAutoNeg, PYSNMP_MODULE_ID=tpt_port_config_objs, FailoverAction=FailoverAction, portConfigFailover=portConfigFailover, portConfigEntry=portConfigEntry)
